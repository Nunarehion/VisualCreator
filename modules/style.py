from _import import *

'''в этом разделе хранятся стандарты цветов'''
color = adict()
#стандартные цвета
color.std = adict()
color.std.white = '#ffffff'
color.std.black = '#000000'
color.std.red   = 'red'


#основные цвета
color.main = adict()
color.main.black = "#1e1f21"

'''набор цветовых палитр'''
color.social = adict(
  #синий
  facebook  = '#3B5999',
  messenger = '#0084FF',
  twiter    = '#55ACEE',
  linkedin  = '#0077B5',
  skype     = '#00AFF0',
  drowbox   = '#007EE5',
  #orange
  google    = '#DD4B39',
  youtube   = '#EB4924',
  redit     = '#FF5700',
  #ruse
  foursquare= '#F94877',
  dibbble   = '#EA4C89',
  flikr     = '#FF0084',
  #red
  quora     = '#B92B27',
  yelp      = '#AF0606',
  weido     = '#DF2029',
  instagram = '#E4405F',
  #green
  whatsup   = '#25D366',
  wechat    = '#09B83E',
  line      = '#00C300',
  medium    = '#02B875',
  vine      = '#00B489',
  #black
  bihance   = '#131418',
  #yellow
  snapchat  = '#FFFC00
  )
color.castom = adict(
  black = adict(
    a = '#000000',
    a001 = '#131418',
    a002 = '#1C1C1C',
    a003 = '#1D1D1D'
  ),
  mblack = adict(
    a001 = '#34495E',
    a002 = '#2C3E50',
    a003 = '#303A52',
    a004 = '#364F6B',
    a005 = '#1B262C',
    a006 = '#204051'
  ),
  mgray = adict(
    a001 = '#323232',
    a002 = '#263238',
    a003 = '#37474F',
    a004 = '#4A5459',
    a005 = '#515C6B',
    a007 = '#313131'
  ),
  gray = adict(
    a300 = '#90A4AE',
    a350 = '#95A5A6',
    a400 = '#78909C',
    a450 = '#7F8C8D',
    a500 = '#607D8B',
    a600 = '#546E7A',
    a700 = '#455A64',
    b400 = '#BDBDBD',
    b500 = '#9E9E9E',
    b600 = '#757575',
    b605 = '#7A7574',
    b610 = '#696969',
    b700 = '#424242',
    c600 = '#778899',
    c610 = '#708090',
    c615 = '#647687'
  ),
  mwhite = adict(
    a100 = '#CFD8DC', #от серго
    a200 = '#B0BEC5',
    b100 = '#BCAAA4', #от корчинего
    b200 = '#BCAAAF',
    b300 = '#A1887F',
    c100 = '#FFCCBC', #от рыжего
    c200 = '#FFAB91',
    c300 = '#FF8A65',
    d090 = '#FFF59D', #от желтого
    d100 = '#FFE0B2', 
    d125 = '#FFF59D',
    d150 = '#FFECB3',
    d200 = '#FFE082',
    e100 = '#C5E1A5', #от зеленого
    e125 = '#C8E6C9',
    e150 = '#A5D6A7',
    e200 = '#C5E1A5',
    e300 = '#AED581',
    e350 = '#81C784',
    f100 = '#B2EBF2', #от синего
    f105 = '#BBDEFB',
    f110 = '#81D4FA',
    f120 = '#90CAF9',
    f125 = '#B3E5FC',
    f150 = '#B2DFDB',
    f175 = '#80DEEA',
    f200 = '#80CBC4',
    g100 = '#C5CAE9', #от фиолетого
    g150 = '#D1C4E9',
    g200 = '#9FA8DA',
    g250 = '#B39DDB',
    h100 = '#FFCDD2', #от красного
    h125 = '#EF9A9A',
    h150 = '#F8BBD0',
    h200 = '#F48FB1'
  ),
  red = adict(
    a700 = '#C2185B',
    a900 = '#B71C1C'
  ),
  feol = adict(
    a700 = '#7B1FA2',
    b700 = '#512DA8'
  ),
  blue = adict(
    a700 = '#303F9F',
    b700 = '#1976D2',
    b900 = '#01579B',
    b950 = '#0D47A1',
    c700 = '#0097A7',
    c800 = '#00838F',
    c900 = '#006064'
  ),
  green = adict(
    a350 = '#00BFA5',
    a500 = '#009688',
    a700 = '#00796B',
    a900 = '#004D40',
    b500 = '#4CAF50',
    b900 = '#1B5E20',
    c500 = '#8BC34A',
    c900 = '#33691E',
    d400 = '#AEEA00'
  ),
  yellow = adict(
    a300 = '#EEFF41',
    a350 = '#FFFF00',
    a500 = '#CDDC39',
    b500 = '#FFEB3B',
    b700 = '#FBC02D',
    b900 = '#F57F17',
    b950 = '#E65100'
  ),
  orange = adict(
    a400 = '#FF7043',
    a700 = '#E64A19',
    a900 = '#BF360C'
  ),
  brown = adict(
    a500 = '#3E2723',
    a900 = '#3E2723'
  ),
  white = adict(
    a50 = '#FAFAFA',
    b50 = '#EFEBE9',
    c50 = '#FBE9E7',
    d50 = '#FFF3E0',
    e50 = '#FFF8E1',
    f50 = '#FFFDE7',
    g50 = '#F9FBE7',
    h50 = '#F1F8E9',
    i50 = '#E8F5E9',
    j50 = '#E0F2F1',
    k50 = '#E0F7FA',
    l50 = '#E1F5FE',
    m50 = '#E3F2FD',
    n50 = '#E8EAF6',
    o50 = '#EDE7F6',
    p50 = '#F3E5F5',
    q50 = '#FCE4EC',
    r50 = '#FFEBEE',
    a01 = '#F5F5F5',
    a02 = '#EDEDED'
  )
)
color.scheme = adict(
  bubblegam = adict(y = '#F4FA9C',
                    r = '#F469A9',
                    v = '#BA53DE',
                    b = '#88BEF5',
                    g = '#57C58D',
                    f = '#1C1C1C',
                    e = '#AAAAAA')
  mysticism = adict(r = '#FC85AE',
                    v = '#9E579D',
                    p = '#FF1493',
                    b = '#574B90',
                    lb= '#6495ED',
                    f = '#1D1D1D',
                    mf ='#303A52',
                    o = '#FF4500',
                    y = '#FFD700',
                    w = '#EDEDED'))
                 


    
    
    

'''в это разделе хранятся наборы стилей для ткинтер'''
style = adict()
style.button = adict() # кнопки
style.button.tools_image_control = adict(bg     = '#16519a',#'#c73f3f',
                                         fg     = '#ffffff',
                                         highlightcolor = 'red',
                                         width  = 9,
                                         height = 1,
                                         font   = ('', 10, 'bold'),
                                         bd = 1,
                                         relief = 'solid',
                                         activebackground = '#f47942',
                                         activeforeground = '#ffdb00')
