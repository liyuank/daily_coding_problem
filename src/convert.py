with open('20190523.txt', 'r') as file:
    data = file.read().replace(',', '，')
    data = data.replace('?', '？')
    data = data.replace('!', '！')
    data = data.replace(':', '：')
    f = open( '/Users/larrykuo/Documents/taiwanyu/20190523', 'w' )
    f.write(data)
    f.close()