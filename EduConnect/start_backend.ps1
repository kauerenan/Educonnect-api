Write-Host "🔄 Reiniciando API EduConnect via Docker..." -ForegroundColor Cyan

# 1. Navegar até a pasta correta
$projeto = "C:\Users\Kaue Renan\Desktop\EduConnect\EduConnect"
Set-Location "$projeto"

# 2. Verifica se Dockerfile existe
if (-Not (Test-Path "$projeto\Dockerfile")) {
    Write-Host "❌ Dockerfile não encontrado em $projeto" -ForegroundColor Red
    exit
}

# 3. Parar e remover container antigo, se existir
docker stop educonnect 2>$null
docker rm educonnect 2>$null

# 4. Build da imagem
Write-Host "🛠️  Build da imagem Docker..." -ForegroundColor Yellow
docker build -t educonnect-api .

# 5. Subir o container
Write-Host "🚀 Subindo container educonnect-api..." -ForegroundColor Green
docker run -d -p 5000:5000 --name educonnect educonnect-api

# 6. Abrir Swagger no navegador (opcional)
Start-Process "http://localhost:5000/apidocs"

Write-Host "✅ API EduConnect reiniciada e Swagger disponível!" -ForegroundColor Green