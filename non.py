tokens =('FRAME','SLOT','TERMINAL','DEFAULT','ALIAS','HOOK','NEWLINE','TAB')
gen_rec={'frame':None,'slot':None,'terminal':None,'alias':None,'default':None}
state={'indent':0,'line':1,'description':None,'token':None,'list_of_types':[]}
def t_error(t):
    "Error handling rule"
    print("Illegal character '%s' in line %s" % (t.value[0], t.lineno))
    t.lexer.skip(1)
def t_TAB(t):
    r'\t '
    return t
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
def t_SLOT(t):
    r'[a-z ]+'
    t.value = t.value.strip()
    return t
def t_FRAME(t):
    r'[A-Z][a-zA-Z0-9 ]+'
    t.value = t.value.strip()
    return t
def t_TERMINAL(t):
    r'[\-][/\\(\)a-zA-Z0-9\,\-\_\@\.\/\#\&\+\-\: ]+'
    t.value = t.value.strip()
    return t
def t_ALIAS(t):
    r'[(][/\\a-zA-Z0-9\,\-\_\@\.\/\#\&\+\- ]+[)]+'
    t.value = str(t.value).strip()[1:-1]
    return t
def t_DEFAULT(t):
    r'[:][/\\a-zA-Z0-9\,\-\_\@\.\/\#\&\+\-\: ]+'
    t.value = t.value.strip()[1:]
    return t
t_HOOK = r'\.\.\.'
def p_attributes(t):
    '''code : frame
            | frame code
            | slot
            | slot code
            | terminal
            | terminal code
            | context
            | context code'''
def p_frame(t):
    'frame : FRAME'
    state['description']=list(t)
    state['token']='frame' 
    if state['indent'] >= len(state['list_of_types'])-1:
        state['list_of_types'].append(list(t)[1])
    else:
        state['list_of_types'][state['indent']+1]=list(t)[1]
    records['is-a'].append((state['list_of_types'][state['indent']],list(t)[1]))
def p_slot(t):
    'slot : SLOT'
    state['description']=list(t)
    state['token']='slot'
    if state['indent'] >= len(state['list_of_types'])-1:
        state['list_of_types'].append(list(t)[1])
    else:
        state['list_of_types'][state['indent']+1]=list(t)[1]
    records['has-a'].append(dict(frame=state['list_of_types'][state['indent']],slot=list(t)[1]))
def p_terminal(t):
    'terminal : TERMINAL'
    state['description']=list(t)
    state['token']='terminal' 
    if state['indent'] >= len(state['list_of_types'])-1:
        state['list_of_types'].append(list(t)[1])
    else:
        state['list_of_types'][state['indent']+1]=list(t)[1]
    records['is-a'].append((state['list_of_types'][state['indent']],list(t)[1]))
def p_alias(t):
    'context : ALIAS'
    records['has-a'][-1]['alias'] = list(t)[1]
    state['description']=list(t)
    state['token']='ALIAS'
def p_default(t):
    'context : DEFAULT'
    state['description']=list(t)
    state['token']='default'
    element = list(t)[1]
    element=element.strip()
    if element.lower() in ['true', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']:
        value=True
    elif element.lower() in ['false', 'f', 'n', 'no', 'nein', 'nope', 'uncertain', 'oh-no']:
        value=False
    elif element.lower() in ['null', '', 'none', 'nothing', 'nada', 'zilch', 'nix', 'not a thing','empty','blank']:
        value=None
    else:
        try:
            value = int(element)
        except ValueError:
            try:
                value = float(element)
            except ValueError:
                value = element
    records['has-a'][-1]['default'] = value
def p_newline(t):
    'context : NEWLINE'
    state['description']=list(t)
    state['token']='newline'
    state['indent']=0
    state['line']+=1
def p_hook(t):
    'context : HOOK'
    state['token']='HOOK'
    state['description']=list(t)
def p_tab(t):
    'context : TAB'
    state['description']=list(t)
    state['token']='tab'
    state['indent']+=1
def p_error(t):
    input("Syntax error at '%s'" % t.value)
def parse_file(slug):
    from ntpath import basename
    state['list_of_types'].append(basename(slug)[:-4])
    parser.parse(str(open(slug, 'r').read()).replace('    ','\t'))
def entity_count(sellerbuyer):
    my_list=[a[1] for a in sellerbuyer]
    my_dict = {i:my_list.count(i) for i in my_list}
    return {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1],reverse=True)}
def undefined_frames(is_a,has_a,has_alias):
    frames= [entity.lower() for entity in entity_count(is_a)]
    properties = entity_count(has_a)
    {k: v for k, v in sorted(properties.items(), key=lambda item: item[1],reverse=True) if k not in frames and v > 1}
if __name__=='__main__':
    import non
    import sys
    import os
    import ply.lex as lex
    import ply.yacc as yacc
    if len(sys.argv) >1:
        file_name=sys.argv[1]
        for arg in sys.argv:
            if not (arg == sys.argv[0] or arg == sys.argv[1]):
                file_name += ' ' + arg
        file_name+='.non'
    for path in sys.path:
        if not path.endswith(".zip"):
            for file in os.listdir(path):
                if (len(sys.argv) >1 and file_name==file) or (len(sys.argv) ==1 and file.endswith('.non')):
                    records={'is-a':[],'has-a':[]}
                    lexer = lex.lex()
                    parser = yacc.yacc()
                    state={'indent':0,'line':1,'description':None,'token':None,'list_of_types':[]}
                    print()
                    print('target:',os.path.join(path, file))
                    print()
                    parse_file(os.path.join(path, file))
                    import pprint
                    pprint.pprint(records)
    
    