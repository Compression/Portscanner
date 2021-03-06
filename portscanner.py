import optparse
parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')

parser.add_option('-H', dest='tgtHost', type='string', help='Specify target port')

parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')

(options, args) = parser.parser_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort

if (tgtHost == None) | (tgtPort == None):
  print parser.usage
  exit(0)
