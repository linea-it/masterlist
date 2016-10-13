import sys
import os
import datetime
import argparse
import shutil
import json
import logging.config
import numpy as np
from astropy.io import ascii
from astropy.table import Table


# ==================================================
def setup_logging(default_path='logging.json',
                  default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """Log all output data."""

    try:  # Python 2.7+
        from logging import NullHandler
    except ImportError:
        class NullHandler(logging.Handler):
            """Class null handler."""

            def emit(self, record):
                """Emit."""
                pass
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            myconfig = json.load(f)
        logging.config.dictConfig(myconfig)
    else:
        logging.basicConfig(level=default_level)

    return


# ==================================================
def read_csv(file_input_csv):
    """Read file of strong lens candidates."""

    # check if data file exists and then read it in.
    if os.path.isfile(file_input_csv):
        data_csv = Table(ascii.read(file_input_csv,
                                guess=True,
                                header_start=0,
                                data_start=1))
    else:
        log.error("... Not a file that can be read in. Please check format")
        return -1

    return data_csv


# ==================================================
def read_json(file_input_json):
    """Read json file to dictionary.

    input:  name of a json file (string)
    output: dictionary
    """

    with open(file_input_json) as data_file:
        data_json = json.load(data_file)

    return data_json


# ==================================================
def save_json(data_json, file_output_json):
    """Save json to file."""

    with open(file_output_json, 'w') as outfile:
        json.dump(data_json, outfile, sort_keys=False, indent=4)

    return


# ==================================================
def convert_list_to_dictionary(data_csv_new):
    """Convert a list (csv) to dictionary format."""

    # empty list of objects
    masterlist_new = []

    # loop over systems
    nb_system = len(data_csv_new)
    for i in range(nb_system):

        # create template input dictionary
        system_dict = {}
        system_dict["model"] = "candidates.candidate"
        system_dict["pk"] = -1 # updated when appended to old list

        # create template fields dictionary
        system_fields = {}

        # add system variables from csv file to dictionary
        # required variables
        try:
            system_fields["ra"] = data_csv_new["ra"][i] # float64 # required
            system_fields["dec"] = data_csv_new["dec"][i] # float64 # required
            system_fields["rank"] = data_csv_new["rank"][i] # int64 # required
            system_fields["data_season"] = data_csv_new["data_season"][i] # str, eg "SV"   # required
        except:
            log.error("Ra, Dec or rank is not available in the new list; these are required.")
            log.error("Exiting.")
            log.info(" ")
            sys.exit()

        # optional variables
        try:
            system_fields["thumb"] = data_csv_new["thumb"][i] # "thumb" : "DES0056-4831_14403533_-48803359.png",
        except:
            log.warning("... Option, 'thumb', not available")
            pass
        try:
            system_fields["object_id"] = data_csv_new["object_id"][i] # "DESJ000-001", # this can be drawn from the RA/Dec?
        except:
            log.warning("... Option, 'object_id', not available")
            pass
        try:
            system_fields["vis_start"] = data_csv_new["vis_start"][i] # str, "MM/DD/YYY"
        except:
            log.warning("... Option, 'vis_start', not available")
            pass
        try:
            system_fields["vis_end"] = data_csv_new["vis_end"][i] #str, "MM/DD/YYY"
        except:
            log.warning("... Option, 'vis_end', not available")
            pass
        try:
            system_fields["followup_date"] = data_csv_new["followup_date"][i]# str, "MM/DD/YYYY"
        except:
            log.warning("... Option, 'followup_date', not available")
            pass
        try:
            system_fields["followup_facility"] = facility_csv_new["followup_facility"][i] # str, "Magellan"
        except:
            log.warning("... Option, 'followup_facility', not available")
            pass
        try:
            system_fields["followup_success"] = facility_csv_new["followup_success"][i] # str, "fail/success"
        except:
            log.warning("... Option, 'followup_success', not available")
            pass

        log.info(" ")

        # add template the fields field of system_dict
        system_dict["fields"] = system_fields

        # add system to new masterlist
        masterlist_new.append(system_dict)

    return masterlist_new


# ==================================================
def append_json(data_json_original, data_json_new):
    """Append items to a JSON file.

    pk: unique id variable for the database

    """

    # assign last pk
    last_pk = data_json_original[-1]["pk"]

    # loop over items in data file of new objects
    pk_new = last_pk + 1
    for system_new in data_json_new:

        # update pk
        system_new["pk"] = pk_new

        #update original list with new system
        data_json_original.append(system_new)

        # increment pk
        pk_new += 1

    # create new list
    data_json_updated = data_json_original

    return data_json_updated


# ==================================================
def create_backup_filename():
    """Create filename for backup file."""

    #define backup directory
    path_backup = "backup/"

    # --------------------------------------
    # check if a backup file for today exists
    # --------------------------------------
    # get today's date
    date_today = str(datetime.date.today()).replace("-","")

    # get list of files in directory
    backup_file_list = [f for f in os.listdir(path_backup) if os.path.isfile(os.path.join(path_backup, f))]

    # loop over filename options
    # check if there's a backup file for today with a given number
    for i in range(100):
        date_today_tmp = date_today + "_" + str(i).zfill(3)
        file_backup = "initial_data_backup_" + date_today_tmp + ".json"

        # check if the filename with a given appended
        # number is in the list of existing files
        if file_backup not in backup_file_list:
            break

    # finalize backup name
    file_output_backup = path_backup + file_backup

    return file_output_backup


# ==================================================
def find_duplicates(data_json_original, data_json_new):
    """Find duplicates in new data, with respect to the original data.."""

    # create list as set of flags
    nb_new = len(data_json_new)
    preserve_list = np.zeros(nb_new)

    # Loop over new objects
    for system_new, i_new in zip(data_json_new, range(nb_new)):

        # Loop over original objects
        for system_original in data_json_original:

            # compare features to test duplication
            compare_ra = system_new["ra"] == system_original["ra"]
            compare_dec = system_new["dec"] == system_original["dec"]
            compare_tot = compare_ra & compare_dec
            if not compare_tot:
                preserve_list[i_new] = 1

    return preserve_list


# ==================================================
def remove_duplicates(data_json_new, preserve_list):
    """Remove duplicates from the new input list."""

    # measure number of Falses (0) in the preserve_list
    check_zero_false = np.where(preserve_list == 0)[0]
    nb_zero_false = len(check_zero_false)

    # if there are some to remove, remove them
    if nb_zero_false > 0:
        data_new_final = data_json_new[check_zero_false]
    elif nb_zero_false == 0:
        data_new_final = data_json_new

    return data_final_new


# ==================================================
def read_input_command_line():
    """Read Inputs from Command Line Options."""

    # create help, default and destination dictionaries for the parser
    parse_help = {
                  "input": "input file name",
    #              "verbose": "increase output verbosity",
                  "backup": "create a backup of the masterlist only",
                  "test": "test appending a list"
                  }
    parse_default = {
                     "input": None,
    #                 "verbose": False,
                     "backup": False,
                     "test": False
                     }
    parse_dest = {
                  "input": "i",
    #              "verbose": "v",
                  "backup": "b",
                  "test": "t"
                  }

    # Description of the parser
    description = "description: update the masterlist by adding a list of objects from an input file."

    # Define parser
    parser = argparse.ArgumentParser(description=description)

    # Add arguments to parser
    # parser.add_argument("-v", "--verbose",
    #                    help=parse_help["verbose"],
    #                    default=parse_default["verbose"],
    #                    action="store_true",
    #                    dest=parse_dest["verbose"])
    parser.add_argument("-t", "--test",
                        help=parse_help["test"],
                        default=parse_default["test"],
                        dest=parse_dest["test"],
                        action="store_true",
                        required=False
                        )
    parser.add_argument("-b", "--backup",
                        help=parse_help["backup"],
                        default=parse_default["backup"],
                        dest=parse_dest["backup"],
                        action="store_true",
                        required=False
                        )
    parser.add_argument("-i", "--input",
                        help=parse_help["input"],
                        dest=parse_dest["input"],
                        required=False
                        )

    # Define argument set from parser
    args = parser.parse_args()

    return args


# ==================================================
def process_update():
    """Combine all elements in to processing an update."""

    # read from commandline
    args = read_input_command_line()

    # define variables for arguments
    backup = args.b
    test = args.t
    file_input = args.i
    file_input_bool = (file_input is not None)

    if not backup  and not file_input_bool:
        log.error("Either an input file must be given or this must be a backup.")
        sys.exit(2)


    # file names
    file_json_original = "./masterlist/candidates/fixtures/initial_data.json"
    file_json_test = "./tests/initial_data_test.json"


    # --------------------------------------
    # inputs
    # --------------------------------------
    log.info("==================================================")
    log.info("Inputs and Options")
    log.info("==================================================")
    log.info("... input file (catalog to add): " + str(file_input))
    log.info("... testing?: " + str(test))
    log.info("... backup?: " + str(backup))
    log.info(" ")
    log.info(" ")

    # --------------------------------------
    # read old json file
    # --------------------------------------
    data_json_original = read_json(file_json_original)
    nb_systems_original = len(data_json_original)
    log.info("==================================================")
    log.info("Read original json file")
    log.info("==================================================")
    log.info("... length of original json file: " + str(nb_systems_original))
    log.info(" ")
    log.info(" ")


    # --------------------------------------
    # backup json
    # create backup file name if this is not a test
    # --------------------------------------
    if not test:
        file_backup = create_backup_filename()
        shutil.copyfile(file_json_original, file_backup)
        log.info("==================================================")
        log.info("Backup the original json file")
        log.info("==================================================")
        log.info("... backup file: " + file_backup)
        log.info(" ")
        log.info(" ")

    # --------------------------------------
    # check if this is a backup only
    # exit if backup only
    # --------------------------------------
    if backup:
        log.info("Backup only. No new catalogs.")
        log.info("Exiting.")
        sys.exit(0)

    # --------------------------------------
    # read new list
    # --------------------------------------
    data_csv_new = read_csv(file_input)
    nb_systems_csv_new = len(data_csv_new)
    log.info("==================================================")
    log.info("Read new csv file to be added to catalog")
    log.info("==================================================")
    log.info("... length of csv data file: " + str(nb_systems_csv_new))
    log.info(" ")
    log.info(" ")


    # --------------------------------------
    # convert list to new json
    # --------------------------------------
    data_json_new = convert_list_to_dictionary(data_csv_new)
    nb_systems_json_new = len(data_csv_new)
    log.info("==================================================")
    log.info("Convert CSV to dictionary")
    log.info("==================================================")
    log.info("... length of json data file: " + str(nb_systems_json_new))
    log.info(" ")
    log.info(" ")

    assert nb_systems_csv_new == nb_systems_json_new, "not the same length after conversion"


    # --------------------------------------
    # Remove Duplicates
    # --------------------------------------
    preserve_list = find_duplicates(data_json_original, data_json_new)
    data_final_new = remove_duplicates(data_json_new, preserve_list)
    log.info("==================================================")
    log.info("Remove Duplicates")
    log.info("==================================================")
    log.info("... length of new data file, duplicates removed: " + str(len(data_final_new))
    log.info(" ")
    log.info(" ")


    # --------------------------------------
    # add new json to old json
    # --------------------------------------
    data_json_updated = append_json(data_json_original, data_json_new)
    nb_systems_updated = len(data_json_updated)
    log.info("==================================================")
    log.info("Update JSON dictionary")
    log.info("==================================================")
    log.info("... length of fully updatd json catalog: " + str(nb_systems_updated))
    log.info(" ")
    log.info(" ")


    # --------------------------------------
    # if only a test (dry run) save to different file
    # --------------------------------------
    if test:
        log.info("==================================================")
        log.info("This is a test version")
        log.info("==================================================")
        file_output = file_json_test
    else:
        file_output = file_json_original
    log.info(" ")
    log.info(" ")


    # --------------------------------------
    # save json to file
    # --------------------------------------
    save_json(data_json_updated, file_output)
    log.info("==================================================")
    log.info("Save updated json to file")
    log.info("==================================================")
    log.info("... output file: " + str(file_output))
    log.info(" ")
    log.info(" ")



# ==============================================================================
# Main
# ==============================================================================
if __name__ == '__main__':
    setup_logging()
    log = logging.getLogger(__name__)
    process_update()

