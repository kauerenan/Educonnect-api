Write-Host "Reiniciando API EduConnect via Docker Compose..." -ForegroundColor Cyan

# 1. Navegar até a raiz do projeto
$projeto = "C:\Users\Kaue Renan\Desktop\EduConnect-api"
Set-Location "$projeto"

# 2. Verificar se docker-compose.yml existe
if (-Not (Test-Path "$projeto\docker-compose.yml")) {
    Write-Host "ERRO: docker-compose.yml não encontrado em $projeto" -ForegroundColor Red
    exit
}

# 3. Derrubar containers antigos e volumes
Write-Host "Limpando containers antigos e volumes..." -ForegroundColor DarkYellow
docker-compose down -v

# 4. Build e subida dos serviços (modo destacado)
Write-Host "Construindo e subindo os serviços..." -ForegroundColor Yellow
docker-compose up --build -d

# 5. Aguardar o backend responder
Write-Host "Aguardando backend iniciar..." -ForegroundColor Cyan
$tentativas = 10
$aguardando = $true

while ($tentativas -gt 0 -and $aguardando) {
    try {
        Invoke-RestMethod -Uri "http://localhost:5000/alunos" -Method GET -TimeoutSec 2 | Out-Null
        $aguardando = $false
    } catch {
        Start-Sleep -Seconds 2
        $tentativas--
        Write-Host "Tentando novamente... ($tentativas restantes)" -ForegroundColor DarkCyan
    }
}

if ($aguardando) {
    Write-Host "ERRO: Não foi possível iniciar o backend após várias tentativas." -ForegroundColor Red
    exit
}

# 6. Abrir o Swagger
Start-Process "http://localhost:5000/apidocs"
Write-Host "API EduConnect está no ar em http://localhost:5000/apidocs!" -ForegroundColor Green