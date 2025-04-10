import pandas as pd
import csv

def main():
    with open("hubspot-sales-register.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    
        required_columns = ("Företagsnamn","Årsintäkter","Land/region","Postnummer","Insamlade pengar", "totalt", "Belopp för senaste avtal","Kundnummer","Ansvarig Säljare","Första Köp","Senast Kontaktad","Måltal","OrgId","Kontaktperson","gata")
        for row in reader:

        # Kolla alla värden
            if not all(column in row for column in required_columns):
                print(f"Error: Missing required columns in row {reader.line_num}")
                break

        # Checka värden
            elif any(row[column] == '' for column in required_columns):
                print(f"Error: Empty required columns in row {reader.line_num}")
                break

        else:
            # Alla värden finns med i listan.
            print("All rows have correct attributes.")

def main2():      
    with open("hubspot-crm-exports-all-contacts-2023-02-21.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    
            required_columns = ("Record ID","First Name","Last Name","Annual Revenue","Average Pageviews","Became a Customer Date","Became a Lead Date","Became a Marketing Qualified Lead Date","Became a Sales Qualified Lead Date","Became a Subscriber Date","Became an Evangelist Date","Became an Opportunity Date","Became an Other Lifecycle Date","Buying Role","Buying Role Option","Campaign of last booking in meetings tool","City","Close Date","Company domain name","Company Name","Company size","Contact owner","Contact priority","Contact unworked","Country/Region","Create Date","Created by user ID","Currently in Sequence","Currently in workflow","Date of birth","Date of last meeting booked in meetings tool","Days To Close","Degree","Domain name","Domain to which registration email was sent","Email","Email address automated quarantine reason","Email address quarantine reason","Email Address Quarantined","Email Confirmed","Email Domain","Email hard bounce reason","Event Revenue","Facebook click id","Fax Number","Field of study","First Conversion","First Conversion Date","First Deal Created Date","First marketing email click date","First marketing email open date","First marketing email reply date","First marketing email send date","First Page Seen","First Referring Site","First Touch Converting Campaign","Gender","Google ad click id","Graduation date","HubSpot Score","HubSpot Team","höbbela","Industry","Invalid email address","IP City","IP Country","IP Country Code","IP State Code/Region Code","IP State/Region","IP Timezone","Job function","Job Title","Last Activity Date","Last Contacted","Last Engagement Date","Last marketing email click date","Last marketing email name","Last marketing email open date","Last marketing email reply date","Last marketing email send date","Last Modified Date","Last NPS survey comment","Last NPS survey date","Last NPS survey rating","Last Page Seen","Last Referring Site","Last sequence ended date","Last sequence enrolled","Last sequence enrolled date","Last Touch Converting Campaign","Latest Source","Latest Source Date","Latest Source Drill-Down 1","Latest Source Drill-Down 2","Lead Rating","Lead Status","Legal basis for processing contact's data","Lifecycle Stage","Likelihood to close","Marital Status","Marketing contact until next update","Marketing email confirmation status","Marketing emails bounced","Marketing emails clicked","Marketing emails delivered","Marketing emails opened","Marketing emails replied","Medium of last booking in meetings tool","Membership Notes","Message","Military status","Mobile Phone Number","Next Activity Date","Number of Associated Deals","Number of Employees","Number of event completions","Number of Form Submissions","Number of Pageviews","Number of Sales Activities","Number of sequences enrolled","Number of Sessions","Number of times contacted","Number of Unique Forms Submitted","Object create date/time","Opted out of email: Customer Service Communication","Original Source","Original Source Drill-Down 1","Original Source Drill-Down 2","Owner Assigned Date","Persona","Phone Number","Postal Code","Predictive Lead Score","Preferred language","Private e-mail address","Recent Conversion","Recent Conversion Date","Recent Deal Amount","Recent Deal Close Date","Recent Sales Email Clicked Date","Recent Sales Email Opened Date","Recent Sales Email Replied Date","Registered At","Relationship Status","Salutation","School","Sends Since Last Engagement","Seniority","Source of last booking in meetings tool","Start date","State/Region","Status","Street Address","Time between contact creation and deal close (HH:mm:ss)","Time between contact creation and deal creation (HH:mm:ss)","Time First Seen","Time Last Seen","Time of First Session","Time of Last Session","Time registration email was sent","Time to move from lead to customer (HH:mm:ss)","Time to move from marketing qualified lead to customer (HH:mm:ss)","Time to move from opportunity to customer (HH:mm:ss)","Time to move from sales qualified lead to customer (HH:mm:ss)","Time to move from subscriber to customer (HH:mm:ss)","Time Zone","Total Revenue","Twitter Username","Unsubscribed from all email","Website URL","WhatsApp Phone Number","Work email","Associated Company","Associated Deal","Associated Ticket","Associated Payment","Associated Subscription","Associated Company IDs","Associated Deal IDs","Associated Ticket IDs","Associated Payment IDs","Associated Subscription IDs")
            for row in reader:

            #Kolla alla värden
                if not all(column in row for column in required_columns):
                    print(f"Error: Missing required columns in row {reader.line_num}")
                    break

                #Checka värden
                elif any(row[column] == '' for column in required_columns):
                    print(f"Error: Empty required columns in row {reader.line_num}")
                    break

            else:
                #Alla värden finns med i listan.
                   print("All rows have correct attributes.")
        
main2()