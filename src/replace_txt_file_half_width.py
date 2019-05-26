# to replace half width punctuation marks to full width

f = open( '/Users/larrykuo/Documents/taiwanyu/0523', 'r' )
str = f.read()
f = open( '/Users/larrykuo/Documents/taiwanyu/20190523.txt', 'w' )
f.write(str.replace(',', '，'))
f.close()


f = open( '/Users/larrykuo/Documents/taiwanyu/20190523.txt', 'r' )
str = f.read()
f = open( '/Users/larrykuo/Documents/taiwanyu/20190523.txt', 'w' )
f.write(str.replace('?', '？'))
f.close()


f = open( '/Users/larrykuo/Documents/taiwanyu/20190523.txt', 'r' )
str = f.read()
f = open( '/Users/larrykuo/Documents/taiwanyu/20190523.txt', 'w' )
f.write(str.replace('!', '！'))
f.close()

f = open( '/Users/larrykuo/Documents/taiwanyu/20190523.txt', 'r' )
str = f.read()
f = open( '/Users/larrykuo/Documents/taiwanyu/20190523.txt', 'w' )
f.write(str.replace(':', '：'))

f.close() 
