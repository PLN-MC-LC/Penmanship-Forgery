from pathlib import Path
import kagglehub

# Define a pasta 'data' no mesmo diretório onde este script está salvo
pasta_destino = Path(__file__).resolve().parent / "data"

# Faz o download diretamente para a pasta escolhida
path = kagglehub.dataset_download(
    "shreelakshmigp/cedardataset",
    output_dir=str(pasta_destino)
)

print("Path to dataset files:", path)
