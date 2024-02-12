# Implementazione di un lettore di immagini JPEG

Questo repository contiene due implementazioni Python di un lettore di immagini JPEG:

- **JPEG_image_reader:** versione sequenziale del lettore;
   
- **JPEG_image_reader_par:** verione parallela del lettore. In questa versione, grazie alla creazione di un numero di processi pari ai core logici e alla asincronia, sono state parallelizzate le operazioni di lettura e salvataggio delle immagini.

## Parametri di configurazione
I parametri che si possono variare per ottenere diverse configurazioni sono:

- **INPUT_IMAGES_RELATIVE_PATH:** Percorso relativo contenente le immagini JPEG/JPG da leggere;

- **OUTPUT_IMAGES_RELATIVE_PATH:** Percorso relativo su cui salvare le immagini in versione bitmap;

- **IMAGES_NUMBER:** Numero di immagini da leggere dalla cartella.
