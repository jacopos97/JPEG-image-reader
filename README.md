# Implementazione di un lettore di immagini JPEG

Questo repository contiene due implementazioni Python di un lettore di immagini JPEG:

- **JPEG_image_reader:** versione sequenziale del lettore;
   
- **JPEG_image_reader_par:** versione parallela del lettore. In questa versione, grazie al multiprocessing e all'asincronia, sono state rese parallele le operazioni di lettura e salvataggio.

## Parametri di configurazione
I parametri che si possono variare per ottenere diverse configurazioni sono:

- **INPUT_IMAGES_RELATIVE_PATH:** Percorso relativo delle immagini JPEG/JPG da leggere;

- **OUTPUT_IMAGES_RELATIVE_PATH:** Percorso relativo in cui salvare le immagini in versione bitmap;

- **IMAGES_NUMBER:** Numero di immagini da leggere dalla cartella.

- **NUM_WORKERS:** (Solo per la versione parallela) Numero di processi utilizzati per parallelizzare le operazioni di lettura e salvataggio.
