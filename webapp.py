from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.template_global(name='zip')
def _zip(*args, **kwargs):
  return __builtins__.zip(*args, **kwargs)

@app.route('/')
def root():
  return render_template('home.html')


@app.route('/suggestions')
def suggestions():
  pictures = ['bqm55','redmi3pro','redminote4','sonyxcompact','redmi3x','motoe3'] 
  brand = ['bq','xiaomi','xiaomi','sony','xiaomi','motorola']
  model = ['BQ Aquaris M5.5','Xiaomi Redmi 3 pro','Xiaomi Redmi Note 4','Sony X Compact','Xiaomi Redmi 3x','Motorola E3']
  pictures1 = ['galaxys7edge','z5','sonyxz','mi5splus','g5','xperiaxperformance'] 
  brand1 = ['samsung','sony','sony','xiaomi','lg','sony']
  model1 = ['Samsung Galaxy s7 Edge','Sony Xperia Z5','Sony XZ','Xiaomi Mi5s Plus','LG G5','Sony Xperia X Performance']
  return render_template('suggestions.html', pictures_brand_model =
  zip(pictures,brand,model), pictures1_brand1_model1 = zip(pictures1,brand1,model1)),200

@app.route('/brands')
def brands():
  pictures = ['samsung','sony','lg','nokia','motorola','bq','iphone','xiaomi']
  return render_template('brands.html', pictures = pictures)

@app.route('/links')
def links():
  pictures = ['Samsung mobile','Sonymobile','LG Mobile Devices','Nokia Phones','Moto Smartphones','BQ Smartphones','iPhone - Apple','Xiaomi China - Global Home']
  link = ['http://www.samsung.com/uk/home','http://sonymobile.com/gb/products/phones',
  'http://www.lg.com/uk/mobile','http://www.nokia.es','https://www.motorola.com/us/products/moto-smartphones',
  'http://www.bq.com/en','http://www.apple.com/iphone/','http://www.mi.com/en/']
  return render_template('links.html', pictures_links = zip(pictures,link))

@app.route('/samsung')
def samsung():
  specs = ['5.1"/5,5"QHD','4Gb RAM','12Mpx','3000/3600mAh','2.3Ghz']
  specs1 = ['5.1"QHD','3Gb RAM','16Mpx','2550mAh','2.15Ghz']
  specs2 = ['5.7"QHD','4Gb RAM','16Mpx','3000mAh','2.1Ghz']
  specs3 = ['5.2"FHD','2Gb RAM','13Mpx','2900mAh','1.6Ghz']
  specs4 = ['4.7"HD','1.5Gb RAM','13Mpx','2300mAh','1.5Ghz'] #A3
  specs5 = ['5.2"HD','2Gb RAM','13Mpx','3100mAh','1.2Ghz']#j5
  specs6 = ['5.0"HD','1.5Gb RAM','8Mpx','2600mAh','1.3Ghz']#j3
  return render_template('samsung.html', specs = specs, specs1=specs1, specs2 =
  specs2, specs3 = specs3, specs4 = specs4, specs5 = specs5, specs6 = specs6)

@app.route('/sony')
def sony():  
  specs = ['5.2"FHD','3Gb RAM','23Mpx','2900mAh','2.3Ghz']#z5
  specs1 = ['5.0"FHD','3Gb RAM','23Mpx','2700mAh','2.15Ghz']#Xperformance
  specs2 = ['5.2"FHD','3Gb RAM','23Mpx','2900mAh','2.1Ghz']#XZ
  specs3 = ['4.6"HD','3Gb RAM','23Mpx','2700mAh','1.6Ghz']#xcompact
  specs4 = ['5.0"HD','1.5Gb RAM','13Mpx','2300mAh','1.3Ghz'] #xperiae5
  specs5 = ['5.0"HD','2Gb RAM','13Mpx','2400mAh','1.2Ghz']#m4aqua
  return render_template('sony.html', specs = specs, specs1=specs1, specs2 =
  specs2, specs3 = specs3, specs4 = specs4, specs5 = specs5)

@app.route('/lg')
def lg():
  
  specs = ['5.3"QHD','4Gb RAM','16Mpx','2800mAh','2.3Ghz']
  specs1 = ['5.5"QHD','3Gb RAM','16Mpx','3000mAh','1.8Ghz']
  specs2 = ['5.2"FHD','2Gb RAM','13Mpx','2520mAh','1.14Ghz']
  specs3 = ['5.2"FHD','2Gb RAM','13Mpx','2900mAh','1.6Ghz']
  specs4 = ['5"HD','1.5Gb RAM','8Mpx','2125mAh','1.3Ghz'] 
  specs5 = ['4.7"HD','1Gb RAM','8Mpx','2100mAh','1.2Ghz']
  return render_template('lg.html', specs = specs, specs1=specs1, specs2 =
  specs2, specs3 = specs3, specs4 = specs4, specs5 = specs5)


@app.route('/nokia')
def nokia():
  
  specs = ['6.0"FHD','2Gb RAM','20Mpx','3400mAh','2.2Ghz']
  specs1 = ['4.7"WVGA','512Mb RAM','5Mpx','2000mAh','1.2Ghz']
  specs2 = ['5"HD','1Gb RAM','10Mpx','2200mAh','1.2Ghz']
  specs3 = ['4"WVGA','512Mb RAM','3Mpx','1500mAh','1.0Ghz']
  specs4 = ['2.4"','30Mb RAM','2Mpx','1200mAh'] 
  return render_template('nokia.html', specs = specs, specs1=specs1, specs2 =
  specs2, specs3 = specs3, specs4 = specs4)


@app.route('/motorola')
def motorola():
  
  specs = ['5.4"QHD','3Gb RAM','21Mpx','3760mAh','2.0Ghz']
  specs1 = ['5.4"QHD','3Gb RAM','21Mpx','3760mAh','2.0Ghz']
  specs2 = ['5.5"FHD','3Gb RAM','16Mpx','3510mAh','2.0Ghz']
  specs3 = ['5.5"FHD','2Gb RAM','13Mpx','3000mAh','1.5Ghz']
  specs4 = ['5"HD','1Gb RAM','8Mpx','2800mAh','1.0Ghz'] 
  return render_template('motorola.html', specs = specs, specs1=specs1, specs2 =
  specs2, specs3 = specs3, specs4 = specs4)

@app.route('/bq')
def bq():
  
  specs = ['5"FHD','3Gb RAM','16Mpx','3200mAh','1.8Ghz']
  specs1 = ['5"HD','3Gb RAM','16Mpx','3050mAh','1.4Ghz']
  specs2 = ['5"HD','2Gb RAM','8Mpx','3080mAh','1.4Ghz']
  specs3 = ['5.5"FHD','3Gb RAM','13Mpx','3620mAh','1.5Ghz']
  specs4 = ['5"HD','2Gb RAM','13Mpx','2850mAh','1.4Ghz'] 
  return render_template('bq.html', specs = specs, specs1=specs1, specs2 =
  specs2, specs3 = specs3, specs4 = specs4,)

@app.route('/xiaomi')
def xiaomi():
  
  specs = ['5.7"FHD','6Gb RAM','13Mpx','3800mAh','2.35Ghz']
  specs1 = ['5.5"FHD','4Gb RAM','13Mpx','4050mAh','2.3Ghz']
  specs2 = ['5.5"FHD','3Gb RAM','13Mpx','4100mAh','2.1Ghz']
  specs3 = ['5FHD','3Gb RAM','13Mpx','4100mAh','1.5Ghz']
  specs4 = ['5HD','2Gb RAM','13Mpx','4100mAh','1.4Ghz'] 
  return render_template('xiaomi.html', specs = specs, specs1=specs1, specs2 =
  specs2, specs3 = specs3, specs4 = specs4)

@app.route('/iphone')
def iPhone():
  
  specs = ['5.5"FHD','3Gb RAM','12Mpx','2900mAh','2.23Ghz']
  specs1 = ['4.7"HD','2Gb RAM','12Mpx','1960mAh','1.8Ghz']
  specs2 = ['4.7"HD','2Gb RAM','12Mpx','1715mAh','1.84Ghz']
  specs3 = ['4"HD','2Gb RAM','12Mpx','1624mAh','1.84Ghz']
  specs4 = ['4"HD','1Gb RAM','8Mpx','15260mAh','1.3Ghz'] 
  return render_template('iphone.html', specs = specs, specs1=specs1, specs2 =
  specs2, specs3 = specs3, specs4 = specs4)
  


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
