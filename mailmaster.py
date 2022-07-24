import imaplib
import email
from email import header as hdr
host= 'imap.gmail.com'
server = imaplib.IMAP4_SSL(host)


class fetcher():
    def login(self, *credentials):
       login, atoken = credentials
       server.login(login, atoken)

    def fetch(self, spec_mail, mailbox="INBOX"):
        messages = []
        server.select(mailbox)
        _, selected_mails = server.search(None, '(FROM "'+spec_mail+'")')
        for num in selected_mails[0].split():
            _, data = server.fetch(num , '(RFC822)')
            _, bytes_data = data[0]

            email_message = email.message_from_bytes(bytes_data)
            print("\n===========================================")
            subject = hdr.decode_header(email_message["subject"])
            print("Subject: ",subject)
            print("From: ",email_message["from"])
            print("Date: ",email_message["date"])
            for part in email_message.walk():
                if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                    message_raw = part.get_payload(decode=True)
                    text = message_raw.decode()
                    print("Message: \n", text)
                    print("==========================================\n")
                    messages.append([subject[0][0], text])
                    break

        return messages

    def logout(self):
        server.logout()


if __name__ == '__main__':
    print('Module is not independent and will run only with credentials master')
