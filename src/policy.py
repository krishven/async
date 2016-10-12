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
    result = {}
    result['value'] = False
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

        temp = database['5']
        rescond = True
        rc=rule.find('resourceCondition')
        for attrName, attrValue in rc.items():
            #print "%s = %s" % (attrName, attrValue)
            if "<" not in attrValue and ">" not in attrValue:
                rescond = rescond and temp[attrName] == attrValue
            elif "<" in attrValue:
                rescond = rescond and int(temp[attrName]) < int(attrValue[1:])
            elif ">" in attrValue:
                rescond = rescond and int(temp[attrName]) > int(attrValue[1:])

        print(subcond and rescond)
        result['value'] = result['value'] or (subcond and rescond)

        if result['value'] == True:
            su=rule.find('subjectUpdate')
            if su != None:
                for attrName, attrValue in su.items():
                    result['type'] = 'subject'
                    result['attrName'] = attrName
                    result['attrValue'] = attrValue
                    break
            ru=rule.find('resourceUpdate')
            if ru != None:
                for attrName, attrValue in ru.items():
                    result['type'] = 'resource'
                    result['attrName'] = attrName
                    result['attrValue'] = attrValue
                    break
            break

        #print('resource condition', rc.attrib)
        #act=rule.find('action')
        #print('action', act.attrib)
        #print()

    print('\n')
    print(result['value'])
    print(result['type'])
    print(result['attrName'])
    print(result['attrValue'])

initDB()
main()