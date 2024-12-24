# Docker 이미지 빌드
cd /work/neojune # neejune 경로
echo "Building Docker image for neojune_kipris_service..."
docker build -f ./src/install/public/Dockerfile -t neojune_kipris_service:1.0 . # 이미지 이름 설정