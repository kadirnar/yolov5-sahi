# Yolov5 Kullanarak Kendi Nesne Tespit Uygulamasını Yap!

<img height="350" src="/images/torch.png"/>

### 1. Veri Setinin Hazırlanması

Hazır veri setlerini alıp yolo formatına çevirerek direk eğitim yapabilirsiniz. Fakat veriyi kendiniz toplayacaksanız direk bu siteye bakabilirsiniz.

- [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)<br/>

İndirme yapmak için github linki bırakıyorum.

- [theAIGuysCode](https://github.com/theAIGuysCode)<br/>

Sadece iki komut bizim için kafidir. 

```
python main.py downloader --classes Apple Orange --type_csv validation
```
İndirdikten sonra classes dosyasını kontrol et. Fazla classes ismi varsa silin yoksa labels kısmında sıkıntı yaşayabilirsiniz.

Yolo formatına dönüştürüyoruz.
```
python convert_annotations.py
```

Örnek: 
     
```
datasets/ 

      images/
    
          train
            img_000.jpg
            ...
            img_999.jpg 
            
          val
           img_000.jpg
           ...
           img_999.jpg 
           
      labels/
          
          train
            img_000.txt
            ...
            img_999.txt 

          val
            img_000.txt
            ...
            img_999.txt
```

Veri setini işlemlerini bitirdikten sonra data.yaml dosyasını oluşturmamız lazım. 

```
train: datasets/images/train # train dosya yolu
val: datasets/images/val     # test dosya yolu
nc: 2                        # nesne sayısı
names: [ 'Apple', 'Orange' ] # etiket isimleri
```
### Yolov5s Modeli Kullanarak Veri Setimizi Eğitelim
```
yolov5 detect --source images/  #images dosyasına test etmek resimleri atın.
```
100 Epoch ile eğittiğim yolov5s modelin sonuçları:(Yarın 100 epoch sonuçlarını paylaşacağım.)

<img height="250" src="/images/1.jpg"/>  


