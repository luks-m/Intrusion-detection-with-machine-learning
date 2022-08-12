50 epochs

2 neurons : loss: 0.5128 - accuracy: 0.7308 - val_loss: 0.5128 - val_accuracy: 0.7300
3 neurons : loss: 0.3574 - accuracy: 0.8359 - val_loss: 0.3396 - val_accuracy: 0.8466
4 neurons : loss: 0.3637 - accuracy: 0.8302 - val_loss: 0.3592 - val_accuracy: 0.8376
5 neurons : loss: 0.0014 - accuracy: 1.0000 - val_loss: 0.0013 - val_accuracy: 1.0000 --> overfitting

25 epochs : 

2 neurons : loss: 0.5703 - accuracy: 0.7208 - val_loss: 0.5687 - val_accuracy: 0.7263
3 neurons : loss: 0.5337 - accuracy: 0.7337 - val_loss: 0.5325 - val_accuracy: 0.7350
4 neurons: loss: 0.5278 - accuracy: 0.7359 - val_loss: 0.5267 - val_accuracy: 0.7347
5 neurons : loss: 0.2872 - accuracy: 0.8833 - val_loss: 0.1370 - val_accuracy: 0.9747

100 epochs :

2 neurons : loss: 0.5232 - accuracy: 0.7297 - val_loss: 0.5243 - val_accuracy: 0.7284
3 neurons : loss: 6.2996e-05 - accuracy: 1.0000 - val_loss: 5.9360e-05 - val_accuracy: 1.0000 ---> overfitting epoch 23
4 neurons : loss: 1.5381e-05 - accuracy: 1.0000 - val_loss: 1.5039e-05 - val_accuracy: 1.0000 ---> overfitting epoch 18

2 neurons : loss: 0.0114 - accuracy: 0.9996 - val_loss: 0.0109 - val_accuracy: 0.9997
3 neurons : loss: 0.4826 - accuracy: 0.7478 - val_loss: 0.4814 - val_accuracy: 0.7485
4 neurons : loss: 0.1018 - accuracy: 0.9690 - val_loss: 0.0980 - val_accuracy: 0.9713


Differences car on regénère des données aléatoires entre chaque training
Résultats si on entraine toujours sur les mêmes données :

on foxe une base de données (fichier data.txt)
100 epochs :
1 neuron : loss: 0.5866 - accuracy: 0.6254 - val_loss: 0.5884 - val_accuracy: 0.6241 --> rien appris, même valeur depuis le début
2 neurons : loss: 0.0193 - accuracy: 0.9996 - val_loss: 0.0188 - val_accuracy: 0.9995
3 neurons : loss: 1.4735e-05 - accuracy: 1.0000 - val_loss: 1.4797e-05 - val_accuracy: 1.0000 --> overfitting à l'époque 27 : 
    loss: 0.0268 - accuracy: 0.9998 - val_loss: 0.0241 - val_accuracy: 0.9998
4 neurons : loss: 6.5338e-04 - accuracy: 1.0000 - val_loss: 6.0655e-04 - val_accuracy: 1.0000 --> overfitting à l'époque 74 : 
    loss: 0.0064 - accuracy: 0.9996 - val_loss: 0.0050 - val_accuracy: 0.9998
5 neurons : loss: 9.8681e-04 - accuracy: 1.0000 - val_loss: 9.4669e-04 - val_accuracy: 1.0000 --> overfitting à l'époque 30 : 
    loss: 0.0629 - accuracy: 0.9994 - val_loss: 0.0530 - val_accuracy: 0.9995

50 epochs : 
1 neuron :  loss: 0.6112 - accuracy: 0.6383 - val_loss: 0.6122 - val_accuracy: 0.6357 --> rien appris, même valeur depuis le début
2 neurons : loss: 0.4974 - accuracy: 0.7429 - val_loss: 0.5002 - val_accuracy: 0.7423
3 neurons : loss: 0.1317 - accuracy: 0.9663 - val_loss: 0.1311 - val_accuracy: 0.9673
4 neurons : loss: 0.0114 - accuracy: 0.9998 - val_loss: 0.0106 - val_accuracy: 0.9998
5 neurons: loss: 0.0094 - accuracy: 0.9999 - val_loss: 0.0087 - val_accuracy: 0.9999

