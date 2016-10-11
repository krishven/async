import xml.etree.ElementTree as ET
import uuid

database = {}

def initDB():
    tree = ET.parse('database.xml')
    root = tree.getroot()
    for subj in root.iter('subject'):
        temp = {}
        for attrName, attrValue in subj.items():
            temp[attrName] = attrValue
        database[subj.attrib['id']] = temp

    for res in root.iter('resource'):
        temp = {}
        for attrName, attrValue in res.items():
            temp[attrName] = attrValue
        database[res.attrib['id']] = temp
    
    # for x in database:
    #     print (x)
    #     for y in database[x]:
    #         print (y,database[x][y])

def main():
    tree = ET.parse('../config/policy-example.xml')
    root = tree.getroot()
    result = False
    for rule in root.iter('rule'):
        #print('rule', rule.attrib['name'])
        temp = database['6']
        subcond = True
        sc=rule.find('subjectCondition')
        for attrName, attrValue in sc.items():
            #print "%s = %s" % (attrName, attrValue)
            if attrName not in temp:
                print('not exists')
            subcond = subcond and temp[attrName] == attrValue

        temp = database['4']
        rescond = True
        rc=rule.find('resourceCondition')
        for attrName, attrValue in rc.items():
            #print "%s = %s" % (attrName, attrValue)
            if "<" not in attrValue and ">" not in attrValue:
                rescond = rescond and temp[attrName] == attrValue
            elif "<" in attrValue:
                rescond = rescond and int(temp[attrName]) < int(attrValue[1:])
            elif ">" in attrValue:
                rescond = rescond and int(temp[attrName][1:]) > int(attrValue[1:])

        print(subcond and rescond)
        result = result or (subcond and rescond)

        #print('resource condition', rc.attrib)
        act=rule.find('action')
        #print('action', act.attrib)
        su=rule.find('subjectUpdate')
        #if su != None:
            #print('subject update', su.attrib)
        ru=rule.find('resourceUpdate')
        #if ru != None:
            #print('resource update', ru.attrib)
        #print()

    print('Final ',result)


#initDB()
#main()
uid = uuid.uuid4().hex
print(type(uid))