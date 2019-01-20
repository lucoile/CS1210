##    return(' '.join([ word.replace(x, '').replace(y, '.') for x in remove for y in replace for word in text.split()]))
    
##    return(' '.join([ word.translate(word.maketrans('?!', '..', """'s()";-""")) for word in text.split()]))

##    return(' '.join([ w.translate(w.maketrans('?!-', '.. ', """'()";""")) for w in [word.replace("'s", '') for word in text.split()]]))
