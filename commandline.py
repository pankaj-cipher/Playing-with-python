import sys
print(sys.argv)
sys.argv.append(1)
sys.argv.append(2)
print("Through command line sum is=",sys.argv[1]+sys.argv[2])
