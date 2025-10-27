import os
import requests

# Lista de tuplas: (nombre_archivo, url)
videos = [
    ("1.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939400985-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T030441Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=aa30164ed9c28e4fcd500d9638d1627efb900dce06b066f9af0d175bc288f659"),
    ("2.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401047-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T025601Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=3f75bb572e27972cab3aa046574ba103e48f4d72a7a48ba647f53646c37de987"),
    ("3.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401126-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T034920Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=cb41a1ee12352a6cf0020e6386de87fee2cfed4e032b43f7440c2901f9a4b6b4"),
    ("4.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401191-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T040530Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=8927496da670f9cfee5f874d6f04533eed1ee544eff6ba12536a2b0f9b4e2f29"),
    ("5.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401263-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T034639Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=f1036b1e8ccac4b5a15c0bc36cc3950a2eca14962a4a9cc4cbb60aa6a25c8704"),
    ("6.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401300-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T034645Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=0f939b0ae94a153b7c1cb8954f83dba810247d74396172c93021511c9d1c1402"),
    ("7.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401362-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T034908Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=117895c5ec49c9f98d9ea07153425ce8cd0f92691c59fdd117b246dbdc43904c"),
    ("8.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401419-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T040633Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=db227dae6f5da8c37d1317e3a02e56499196bee71fd7141d7b2c267e78ea8d97"),
    ("9.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401458-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T035218Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=f54ff64bf023d61e150cd25679bd9f20039eb23d78932eac1cb2d7cc13b7d7ac"),
    ("10.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939401520-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T041747Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=225314adb1f5f567e7cbae40dbd138da841950f8fa7640f1111dd4eacb3e8526"),
    ("11.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939400245-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T024207Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=c0d6dac4157cdd8c6aa9b30af8a9bc28de1847e3067189682e0402315eb22111"),
    ("12.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939400356-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T040521Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=ac882f442fef7bcf0a581ad52cfe9401c19d63239c094b4bcc5ac78136834be9"),
    ("13.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939464545-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T024656Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=45d48d19b702e12a7f77654c5b297fcd85eb36cd599dc9d0d4ea97a77e8fb6f0"),
    ("14.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939400568-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T024659Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=6d9ff6ecfde6e5ba3433ca45d7656aed500873338966111d09b4a83ed58283e7"),
    ("15.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939400661-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T030645Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=fd86bff19f4c966d1fec1ba325abf504b833b5c428f43b054611021e137e5481"),
    ("16.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939400717-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T024332Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=ba01d1d20b45378b8765e93f751781a73cc6937ee61278bfcab123a06cdd4b74"),
    ("17.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939400794-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T030322Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=b63571fe337ec1675836e04a9579a61c883753dd6b5667dbf0e92746e4a3464f"),
    ("18.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939471836-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T030517Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=bd930f599b321cb7e7512b17402847f53d9de1adef7e8b5d23cd9cee5dd13f53"),
    ("19.mp4","https://gnarus-video.4986a99d4a6ebf7ab87ee6461d95b58b.r2.cloudflarestorage.com/alura/939400880-hd.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250820T033027Z&X-Amz-SignedHeaders=host&X-Amz-Credential=099e678757b68a07f650f27240529bce%2F20250820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=f37140d324f8aae3c0c7291eac79750633e7953c12e0ed587d1ad0c9cf1f0d13")
    # agrega más (nombre, url) aquí...
]

# Ruta donde se guardarán los videos
output_dir = r"D:\aluraPOOAPIS\springjava3"  # CAMBIA por tu ruta deseada
os.makedirs(output_dir, exist_ok=True)

for i, (filename, url) in enumerate(videos, start=1):
    try:
        print(f"Descargando video {i}: {filename}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # lanza excepción si falla la descarga

        filepath = os.path.join(output_dir, filename)

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"✅ Guardado en: {filepath}")
    except Exception as e:
        print(f"❌ Error descargando {filename}: {e}")
