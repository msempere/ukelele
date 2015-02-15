from sys import exit, stderr

def error_message(message, line):
    stderr.write('Error in line {l}: {msg}.\n'.format(l=line, msg=message))
    exit(-1)

def already_defined_message(who, new_line, old_line):
    msg = '"{element}" already defined in line {ol}'.format(element=who, ol=old_line)
    error_message(msg, new_line)

def reserved_word_message(word, line):
    msg = 'Illegal use of reserved word "{element}"'.format(element=word)
    error_message(msg, line)

def error_message_without_line(message):
    stderr.write('Error: {msg}.\n'.format(msg=message))
    exit(-1)

