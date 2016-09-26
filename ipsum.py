from browser import document, alert, console


__version__ = '0.1.1-dev'


WORDS = [
    'لورم',
    'ایپسوم',
    'دلار',
    'سیت',
    'امیت،',
    'کانسکتتور',
    'ادیپی\u200eچینگ',
    'الیت،',
    'سِد',
    'دیام',
    'نانومی',
    'نیب',
    'ایسمود',
    'تینسی\u200cدنت',
    'اوت',
    'لاوریت',
    'دلاری',
    'مگنا',
    'الیکوام',
    'اَرآت',
    'ولوتپات.',
    'اوت',
    'ویسی',
    'انیم',
    'اد',
    'مینیم',
    'ونیام،',
    'کویز',
    'ناسترود',
    'اکسرچی',
    'تاشن',
    'اولام\u200cکورپر',
    'ساچیپیت',
    'لابارتیس',
    'نیسل',
    'اوت',
    'الی\u200cکوئیپ',
    'اکس',
    'ئی',
    'کومودو',
    'کانسکوات.',
    'دوئیس',
    'آئوتیم',
    'ول',
    'ایوم',
    'ایریوره',
    'دلار',
    'این',
    'هندرریت',
    'این',
    'وولپوتایت',
    'ولیت',
    'اسّی',
    'مالستی',
    'کانسکوات،',
    'ول',
    'ایلیوم',
    'دلاره',
    'ایو',
    'فیوگیات',
    'نولا',
    'فاسیلیسی',
    'ات',
    'ورو',
    'اروس',
    'ات',
    'اکومسان',
    'ات',
    'ایوستو',
    'اودیو',
    'دیگنسیم',
    'کوئی',
    'بلاندیت',
    'پرائیسنت',
    'لوپتاتوم',
    'زریل',
    'دلنیت',
    'آوگیو',
    'دوئیس',
    'دلاره',
    'تی',
    'فیوگایت',
    'نولا',
    'فاسیلیسی.']

WORDS_LENGTH = len(WORDS)

def go(ev):
    document['output'].value = '\n\n'.join(' '.join(WORDS[:int(document['words'].value)]) for i in range(int(document['paragraphs'].value)))

document['version'] <= __version__
document['words'].max = document['words'].value = WORDS_LENGTH
document['go'].bind('click', go)
