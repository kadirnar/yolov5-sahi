##  Yolov5+Sahi Kullanarak Yüksek Doğruluklu Nesne Tespit Uygulamasını Yap!
<img height="350" src="/images/torch.png"/>

### Küçük Nesne Tespiti için Yolov5 + SAHİ:
- [Veri Setinin Topla](#veri-setinin-topla)<br/>
- [Veri Setini Yolo Formatına Çevir](#veri-setini-yolo-formatına-çevir)<br/>
- [Yolov5 için Veri Setini Düzenleme ve Yaml Dosyasını Oluşturma](#yolov5-için-veri-setini-düzenleme-ve-yaml-dosyasını-oluşturma)<br/>
- [Yolov5s Modeli Kullanarak Veri Setini Eğit](#yolov5s-modeli-kullanarak-veri-setini-eğit)<br/>
- [Test Sonuçları ve Hataları](#test-sonuçları-ve-hataları)<br/>
- [Modelini Düzeltmek için Çözüm Önerileri](#modelini-düzeltmek-için-çözüm-önerileri)<br/>
- [Yolov5 ve Sahi Algoritması](#yolov5-ve-sahi-algoritması)<br/>
- [Tüm Resimleri Tek Seferde Test Edin](#tüm-resimleri-tek-seferde-test-edin)

### Veri Setinin Topla

Hazır veri setlerini alıp yolo formatına çevirerek direk eğitim yapabilirsiniz. Fakat veriyi kendiniz toplayacaksanız direk bu siteye bakabilirsiniz.

- [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)<br/>

### Veri Setini Yolo Formatına Çevir

- [theAIGuysCode](https://github.com/theAIGuysCode)<br/>

Bu github reposundaki iki komut bizim için yeterli olacaktır.
```
python main.py downloader --classes Apple Orange --type_csv train --limit 1000
```
İndirdikten sonra classes dosyasındaki gereksiz labelleri sil ve python dosyasını çalıştır.

```
python convert_annotations.py
```
### Yolov5 için Veri Setini Düzenleme ve Yaml Dosyasını Oluşturma

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

Veri seti işlemlerini bitirdikten sonra data.yaml dosyasını oluşturmamız lazım. 

```
train: datasets/images/train # train dosya yolu
val: datasets/images/val     # test dosya yolu
nc: 2                        # nesne sayısı
names: [ 'Apple', 'Orange' ] # etiket isimleri
```
### Yolov5s Modeli Kullanarak Veri Setini Eğit
```
yolov5 detect --weights best.pt --source images/  #images dosyasına test etmek resimleri atın.
```
100 Epoch ile eğittiğim yolov5s modelin sonuçları:

<img height="250" src="/images/1.jpg"/>  <img height="250" src="/images/output1.jpg"/> 
 
### Test Sonuçları ve Hataları
Problem:

1. Bazı elmaları grup olarak alması.(1.resim)
2. Acc sonucu ve tespit ettiği görsel sayısı düşük.(2.resim)


### Modelini Düzeltmek için Çözüm Önerileri:

Çözüm:

1. Veri setlerini ve etiketleri open images sitesinden aldığımız için, etiketleme işlemi yaparken hata yapılmış. Apple logosunun olduğu simgeleri de elma olarak etiketlenmişti. Bu yüzden öncellikle veri setini düzenleyip tekrar eğitim yapmamız lazım.

2. Modelimizi/veri setini büyütebiliriz veya parametre değerleri ile oynamalıyız. 

3. Modelimize sahi algoritmasını ekleyebiliriz.

### Yolov5 ve Sahi Algoritması
Veri seti ve etiket hatalarını kesinllikle düzeltmeliyiz. Peki bunları sahi algoritması ile düzeltmek istedeydik nasıl olurdu? Farkettiyseniz tespit ettiği elmaların değerleri biraz düşük. confidence_threshold değerini 0.5 yapsaydık nasıl sonuç verdiğine gelin bakalım.

<img height="300" src="/images/yolov5.png"/>  

Veri setini düzenleyip daha iyi bir model denesek daha iyi olur galiba :( Peki ya Sahi'yi denesek nasıl olur? 🚀 Uçuracak gibi duruyor :)

<img height="300" src="/images/yolov5_sahi.png"/> 

Sahi Algoritmasındaki Parametre Değerleri:
```
result = get_sliced_prediction(
    "images/2.jpg",
    detection_model,
    slice_height = 128,
    slice_width = 128,
    overlap_height_ratio = 0.8,
    overlap_width_ratio = 0.8)
```

Elma nesnesi için 1000+ fazla resim toplarken portakal için 500 resim toplayabilmiştim. Onun doğruluğu tabi ki daha düşük oldu.

<img height="350" src="/images/yolov5-orange.png"/> 

Peki sahi kullanırsak nasıl bir sonuç alırız?

<img height="350" src="/images/yolov5_Sahi_orange.png"/> 

### Tüm Resimleri Tek Seferde Test Edin
(Eklenecek.)
### Referanslar

sahi: https://github.com/obss/sahi

yolov5: https://github.com/fcakyon/yolov5-pip
