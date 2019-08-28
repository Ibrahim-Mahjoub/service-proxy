import os
import csv
import chardet
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from proxy.models import Mask, Service

def get_encoding(fname):
    """
    Returns encoding of file, fname.
    :param fname: string
    :return: string
    """
    file = open(fname, 'rb')
    encoding = chardet.detect(file.read())['encoding']
    return encoding

def not_none(value):
    """
    Returns value iff value is not none.
 
    :param value: string
    """
    if not value:
        raise ValueError("Empty Value")
    return value

def get_service(name):
    """
    Returns service with name, name.
   
    :param name: service name (string)
    :return: service object
    """
    service = Service.objects.get(name=name)

    return service

def create_mask(userId, pseudoId, service):
    """
    Returns the newly created and saved proxy mask object.

    :param userId: user id (string)
    :param pseudoId: pseudonymous id (string)
    :param service: service object
    """
    # create proxy mask
    mask = Mask.objects.create(
        userId = userId,
        pseudoId = pseudoId,
        service=service,
    ) 

    return mask
    


class Command(BaseCommand):
    """
    Createmasks command - used to create proxy mask objects from file.

    File Type: csv

    Format: userId,pseudoId,serviceName
    """

    help = "Used to create proxy masks from csv file. " \
           "(Format: userId,pseudoId,serviceName)"

    def add_arguments(self, parser):
        """
        adding command arguments to command line parser.
        """
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **options):
        """
        Parses csv file and creates corresponding objects from parsed data.
        Note: Parsed data in csv format
        """
        try:
            # csv path argument
            fpath = options['csv_path']
            # checks if file is csv
            if fpath.lower().endswith('csv'):
               encoding = get_encoding(fpath)
               with open(fpath, encoding=encoding) as file:
                   reader = csv.reader(file, delimiter=",")
                   # iterating through each row in csv
                   for row in reader:
                       # creates proxy masks
                       try:
                           # csv entries are stripped of leading and trailing
                           # whitespace
                           service = get_service(not_none(row[2].strip()))
                           _ = create_mask(not_none(row[0].strip()),
                                           not_none(row[1].strip()),
                                           service)
                       except IntegrityError:
                           # duplicate information
                           self.stderr.write(self.style.WARNING(
                               "(Warning) "
                               "Duplicate Information: {}".format(row)))
                       except IndexError:
                           # problem extracting missing information
                           self.stderr.write(self.style.WARNING(
                               "(Warning) Incorrect Format: {}".format(row)))
                       except ValueError:
                           # missing information
                           self.stderr.write(self.style.WARNING(
                               "(Warning) Missing Value: {}".format(row)))
                       except ObjectDoesNotExist:
                           # service does not exist
                           self.stderr.write(self.style.WARNING(
                               "(Warning) " 
                               "Service Does Not Exist: {}".format(row)))
            else:
                # file not csv
                self.stderr.write(self.style.ERROR("(Error) "
                                                   "File not of type csv."))
        except FileNotFoundError:
            # file path does not exist
            self.stderr.write(self.style.ERROR("(Error) File does not exist."))
        except IOError:
            # error reading file
            self.stderr.write(self.style.ERROR("(Error) Error reading file."))
