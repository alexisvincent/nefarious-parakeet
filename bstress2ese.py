import sys

maxVal = 0.
minVal = 0.
maxID  = 0.
minID  = 0.

if ( len(sys.argv) != 2 ):
	print "ERROR: must supply one and only one command line arg"
	print "       - just the PCH fiel name (without extension)"
	exit()

FBASE = sys.argv[1]
#LCID  = sys.argv[2]

f = open( FBASE+'.pch', 'r' )
#maxName = FBASE+'ese_max_lc%02d.pch'%(int(LCID))
maxName = FBASE+'ese_max.pch'
fo1 = open( maxName, 'w' )
#minName = FBASE+'ese_min_lc%02d.pch'%(int(LCID))
minName = FBASE+'ese_min.pch'
fo2 = open( minName, 'w' )

for l in f:
	if ( l.startswith('$ELEMENT STRESSES') ):
		f.next()
		sl0 = f.next()
		sl1 = f.next()
		if ( sl0.startswith('$SUBCASE ID = ') and sl1.startswith( '$ELEMENT TYPE =          34') ):

			fo1.write( '$TITLE   = \n' )
			fo1.write( '$SUBTITLE= \n' )                                                         
			fo1.write( '$LABEL   =STATIC\n' )
			fo1.write( '$ELEMENT STRAIN ENERGIES\n' )
			fo1.write( '$REAL OUTPUT\n' )
			fo1.write( sl0)
			fo1.write( sl1)

			fo2.write( '$TITLE   = \n' )
			fo2.write( '$SUBTITLE= \n' )                                                           
			fo2.write( '$LABEL   =STATIC\n' )
			fo2.write( '$ELEMENT STRAIN ENERGIES\n' )
			fo2.write( '$REAL OUTPUT\n' )
			fo2.write( sl0 )
			fo2.write( sl1 )

			for l1 in f:
				if ( l1.startswith('$') ):
					break
				l1 = l1.split()
				l2 = f.next().split()
				l3 = f.next().split()
				l4 = f.next().split()
				l5 = f.next().split()
				elID = l1[0]
				maxA = l2[3]
				minA = l3[1]
				maxB = l5[1]
				minB = l5[2]
				
				maxAB = maxA
				if ( float(maxB) > float(maxA) ):
					maxAB = maxB
				minAB = minA
				if ( float(minB) < float(minA) ):
					minAB = minB
				if ( float(maxAB) > maxVal ):
				  maxVal = float(maxAB)
				  maxID  = int(elID)
				#maxVal = max(float(maxAB), maxVal)
				if ( float(minAB) < minVal ):
				  minVal = float(minAB)
				  minID  = int(elID)
				#minVal = min(float(minAB), minVal)
				
				spacer = '    '
				if ( float(maxAB)  < 0 ):
					spacer = '   '
				fo1.write( '%10s         '%(elID.strip()) )
				fo1.write( spacer )
				fo1.write( maxAB )
				fo1.write( spacer )
				fo1.write( maxAB )
				fo1.write( spacer )
				fo1.write( maxAB )
				fo1.write( '\n' )
				
				spacer = '    '
				if ( float(minAB)  < 0 ):
					spacer = '   '
				fo2.write( '%10s         '%(elID.strip()) )
				fo2.write( spacer )
				fo2.write( minAB )
				fo2.write( spacer )
				fo2.write( minAB )
				fo2.write( spacer )
				fo2.write( minAB )
				fo2.write( '\n' )
			
			print sl0,
			print "Max Stress value = " + str(maxVal) + " at elId " + str(maxID)
			print "Min Stress value = " + str(minVal) + " at elId " + str(minID)
			print '\n'
			maxVal = 0.
			minVal = 0.

f.close()
fo1.close()
fo2.close()
