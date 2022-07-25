<div align="center">
<h2>
  Yolov5 Modelini Kullanarak Özel Nesne Eğitimi ve SAHI Kullanımı
</h2>
<h4>
    <img width="700" alt="teaser" src="images\logo.png">
</h4>
</div>

Bu yazıda, en popüler YOLO mimarilerinden birisi olan Yolov5 kullanımını göreceğiz. Bu yazıda göreceğiniz konu başlıkları şunlardır:

- [Yolov5 için Özel Veri Seti Oluşturma]()
- [Yolov5-Pip kullanarak Veri Setini Eğitimi]()
- [Yolov5-Pip kullanarak Nesne Tespiti]()
- [SAHI Kullanarak Tespit Sonucunu İyileştirme]()
- [Sonuç]()

### 1. Yolov5 için Özel Veri Seti Oluşturma

Yolov5 modeli için veri seti oluşturmak için 2 seçeneceğimiz var. Veri setini kamera yardımıyla kendimiz oluşturabiliriz veya Kaggle ve Open Images Dataset gibi sitelerden hazırlanmış veri setlerini indirebiliriz. Bu yazıda hazır veri setlerini kullanacağız.

Open Images Dataset platformunu kullanarak veri seti indirme için OIDv4_ToolKit reposunu kullanacağız. Bu repoyu indirmek için git kütüphanesini kullanarak indirme işlemi gerçekleştireceğiz.

```
git clone https://github.com/theAIGuysCode/OIDv4_ToolKit.git
cd OIDv4_ToolKit
pip install -r requirements.txt
```
İndirme ve kütüphane kurumlarını yaptıktan sonra istediğimiz veri setini Open Images Dataset sitesinden bakarak komut satırından indirme işlemini yapacağız.
```
python main.py downloader --classes Apple --type_csv train --limit 1000
```
<img width="700" alt="teaser" src="images\data.png">
İndirme işleminden sonra classes.txt dosyasını class isimlerini düzelttikten sonra label değerlerini yolo formatına dönüştürme işlemi yapacağız.
```
python convert_annotations.py 
```	
Başarılı şekilde indirme ve dönüştürme işlemi yaptıktan OIDv4_ToolKit/OID/Dataset/train klasörü içinde images ve labels klasörleri bulunmaktadır. Eğitim yapmak için train ve validation image ve label dosyalarına ihtiyacımız var. Bunun için yeniden indirme işlemi yapabilirsiniz veya indirilen image ve label dosyalarını train ve validation olarak iki kısıma ayırabilirsiniz.

```
dataset/ 
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
Veri setini hazırladıktan sonra data.yaml dosyasını oluşturmamız gerekiyor. Bizim hazırladığımız images ve labels dosyalarını nerede olduğunu yolov5 modeline bildirmemiz gerekiyor. Data.yaml dosyasımız şu şekilde olmalıdır:
```
train: dataset/images/train # train dosya yolu
val: datasets/images/val     # validation dosya yolu
nc: 1                       # nesne sayısı
names: [ 'Apple' ] # etiket isimleri`
```
### 2. Yolov5-Pip kullanarak Veri Setini Eğitimi
Eğitim yapabilmek için yolov5 kütüphanesini indirmemiz gerekiyor. Bunun için yolov5 kütüphanesinin pip versiyonunu kullanacağız.
```
pip install yolov5
```
Kütüphane indirme işlemi başarılı şekilde yaptıktan train kodunu yazıyoruz.
```
yolov5 train --data dataset/data.yaml --weights yolov5s.pt --batch-size 16 --img 320 --epochs 100
```
### 3. Yolov5-Pip kullanarak Nesne Tespiti
Modelimizin performans parametre sonuçlarını incelledikten bir resim üzerinden tespit işlemi yapıyoruz.
```
yolov5 detect --weights best.pt--source 0 apple.jpg
```
<img width="700" alt="teaser" src="images\yolov5.png">

Hazırladığımız yolo modelinde iki problem gözlenmektedir. 
- Küçük nesneleri tespit edememektedir.
- Büyük kare hatası

Tespit sonucundaki hata oranı düşürmek için büyük modeller tercih edebiliriz. Küçük elmaları tespit etmek için ise veri setine küçük elma resimleri ekleyebiliriz. 
### 4. SAHI Kullanarak Tespit Sonucunu İyileştirme
Modeli optimum hale getirmek yerine SAHI kütüphanesini Yolov5 ile test edeceğiz.
```
!sahi predict - model_type yolov5 - model_path best.pt - source apple.png
```
<img width="700" alt="teaser" src="images\SAHI.png">

SAHI harika bir iş çıkardı ve nerdeyse tüm nesneleri tespit etmektedir. Burada aldığımız boyut hatası tamamen Yolov5 ve veri seti ile ilgilidir. Topladığımız veri setinde toplu elma resimleri tek elma olarak etiketlendiği için böyle bir hata almaktayız. Veri setini kontrol edip manuel silme işlemi veya yolov5 detect kodlarına gidip boxes değerlerinde sınırlanma yaparak bu problemi çözebiliriz. 

### 5. Sonuç 
Bu yazıda şu konuları anlattık:
- Open Images Dataset sitesinden Veri Oluşturmayı
- Yolov5-Pip kullanarak Veri Setini Eğitimi
- Yolov5-Pip kullanarak Nesne Tespiti
- SAHI Kullanarak Tespit Sonucunu İyileştirme

Herhangi bir adım da yaşayacağınız herhangi bir problem de bana sormaktan çekinmeyin.

### Referanslar:
- [Yolov5-Format-Datasets](https://github.com/kadirnar/yolov5-format-datasets)
- [OIDv4_ToolKit](https://github.com/theAIGuysCode/OIDv4_ToolKit)
- [Yolov5-Pip](https://github.com/fcakyon/yolov5-pip)
- [SAHI](https://github.com/obss/sahi)

