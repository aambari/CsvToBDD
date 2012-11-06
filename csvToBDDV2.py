'''
Created on Oct 16, 2012

@author: aambari
'''


def csvToBdd(func, file, width):
    with open( file, 'r')   as f:
        s = f.readline()
        initialStates = s.split(',')[1:]
    
        for line in f:
            eventAndItsStates = line.split(',')
            nextStateCounter = 1
            for state in initialStates:    
                event =  eventAndItsStates[0]
                func(state, event, eventAndItsStates[nextStateCounter], width)
                nextStateCounter+=1

  
    
def formatOutput(initialState, event, nextState, width):
    print (' |' + initialState.strip(' \n').ljust(width)
                   + '|' + event.strip(' \n').ljust(width) 
                   + '|' + nextState.strip(' \n').ljust(width)
                   + '|')

def formatOutput2(initialState, event, nextState, width):
    print("|{:<25}|{:<25}|{:<25}|".format(initialState.strip(), event.strip(), nextState.strip()))

def main(*args):

    csvToBdd(formatOutput2, 'c:\Python\campaign_js_cleaned_for_3_events.csv', 25 )



if __name__ == '__main__':
    import sys
    main(*sys.argv)