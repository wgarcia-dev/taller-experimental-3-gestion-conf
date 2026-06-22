# Deploy notes

## Objetivo

Simular el despliegue del proyecto Django en una carpeta externa usando Docker Compose.

## Evidencia desde GitHub Actions

El workflow `.github/workflows/ci.yml` ejecuta:

1. Instalacion de dependencias.
2. Pruebas con `python manage.py test`.
3. Construccion de la imagen Docker `taller-gestion-conf:ci`.
4. Validacion dentro del contenedor con `docker run --rm taller-gestion-conf:ci python manage.py test`.
5. Exportacion simulada de la imagen con `docker save`.
6. Carga del artefacto `taller-gestion-conf-docker-image`.

Para la captura:

1. Subir la rama a GitHub.
2. Entrar a la pestana **Actions**.
3. Abrir el workflow **CI**.
4. Capturar el job `docker` en verde y el artefacto `taller-gestion-conf-docker-image`.

## Despliegue simulado en carpeta externa

Crear una carpeta fuera del proyecto:

```bash
mkdir C:\deploy-simulado
cd C:\deploy-simulado
```

Descargar o clonar el proyecto:

```bash
git clone <URL_DEL_REPOSITORIO> taller-gestion-conf
cd taller-gestion-conf
```

Cambiar a la rama de trabajo:

```bash
git checkout ci-setup
```

Construir la imagen:

```bash
docker compose build
```

Levantar el contenedor:

```bash
docker compose up
```

Validar desde el navegador:

```text
http://localhost:8000
```

Para detener el despliegue:

```bash
docker compose down
```

## Validacion alternativa

Si solo se necesita comprobar Django dentro del contenedor:

```bash
docker compose run --rm web python manage.py test
```

Resultado esperado:

```text
Ran 10 tests
OK
```
