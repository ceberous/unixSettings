#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from time import localtime, strftime
from datetime import datetime
from pytz import timezone

eastern_tz = timezone('US/Eastern')

import securityDetails

def sendEmail( alertLevel , msg ):

        wFROM = securityDetails.fromGmx
        wTO = securityDetails.toEmail

        wTN = datetime.now( eastern_tz )
        wNow = wTN.strftime( "%Y-%m-%d %H:%M:%S" )
        msg = wNow + "\n\n" + msg

        wMessage = MIMEMultipart()
        wMessage['From'] = wFROM
        wMessage['To'] = wTO
        wMessage['Subject'] = alertLevel
        wMessage.attach( MIMEText( msg ) )
        #print wMessage

        try:
                server = smtplib.SMTP( securityDetails.gmxSMTP , 587 )
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login( wFROM , securityDetails.gmxPass  )
                server.sendmail( wFROM , wTO , wMessage.as_string() )
                server.close()
                print('sent email')
        except:
                print('failed to send email')


sendEmail( "1" , "Haley Is Moving" )