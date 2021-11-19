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

<img height="250" src="/images/1.jpg"/>  <img height="250" src="/images/output1.jpg"/> 

<img height="300" src="/images/2.jpg"/>  <img height="300" src="/images/output2.jpg"/> 

<img height="300" src="/images/3.jpg"/>  <img height="300" src="/images/output3.jpg"/> 

Problem:

1. Bazı elmaları grup olarak alması.(1.resim)
2. Acc sonucu ve tespit ettiği görsel sayısı düşük.(2.resim)

Çözüm:

1. Veri setlerini ve etiketleri open images sitesinden aldığımız için, etiketleme işlemi yaparken hata yapılmış. Apple logosunun olduğu simgeleri de elma olarak etiketlenmişti. Bu yüzden öncellikle veri setini düzenleyip tekrar eğitim yapmamız lazım.

2. Modelimizi/veri setini büyütebiliriz veya parametre değerleri ile oynamalıyız. 

3. Modelimize sahi algoritmasını ekleyebiliriz.
