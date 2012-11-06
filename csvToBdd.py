'''
Created on Oct 16, 2012

@author: aambari
'''


def csvToBdd(file, width):
    f = open( file, 'r')   

    s = f.readline()
    initialStates = s.split(',')[1:]
    
    for line in f.readlines():
        eventAndItsStates = line.split(',')
        nextStateCounter = 1;
        for state in initialStates:    
            event =  eventAndItsStates[0]
            print (' |' + state.strip(' \n').ljust(width)
                   + '|' + event.strip(' \n').ljust(width) 
                   + '|' + eventAndItsStates[nextStateCounter].strip(' \n').ljust(width)
                   + '|')
            nextStateCounter = nextStateCounter + 1
    f.close()
  
    
  


def main(script, *args):
    csvToBdd('c:\Python\cell_js_cleaned_for_3_events.csv', 25 )



if __name__ == '__main__':
    import sys
    main(*sys.argv)