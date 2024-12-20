# System imports
import csv, io, os, sys, json, time, logging.config, configparser
# Third party imports
import praw
import praw.exceptions
import prawcore.exceptions


config = configparser.ConfigParser()
configfile_path = os.path.abspath(os.path.dirname(sys.argv[0]))
configfile_path = os.path.join(configfile_path, 'Subreddit-Flair-Distribution-Counter.cfg')
config.read(configfile_path)
logging.config.fileConfig(configfile_path)

start_time = time.time()

while True:
    try:
        r = praw.Reddit(client_id=config['reddit']['client_id'],
                        client_secret=config['reddit']['client_secret'],
                        user_agent=config['reddit']['user_agent'],
                        username=config['reddit']['username'],
                        password=config['reddit']['password'])
        logging.info('Logged in as {0}.'.format(r.user.me()))
        break
    except prawcore.OAuthException as e:
        logging.error('OAuth Error: {0}'.format(e.description))
        logging.info('If you received an \'invalid_grant\' error, make sure the user and pass are correct \n'
                     'and that they are the same as the account you registered the script with.')
        logging.info('Retrying in 20 seconds, or CTRL+C to stop the script...')
        time.sleep(20)
    except KeyboardInterrupt:
        logging.info('Shutting down due to keyboard interrupt.')
        exit()
    except prawcore.exceptions.ResponseException as e:
        if e.response.status_code == 401:
            logging.error('HTTP 401: Ensure authentication credentials are configured \n'
                          'in Subreddit-Flair-Distribution-Counter.cfg')
        else:
            logging.error('Error: {0}'.format(e))
        exit()
    except Exception as e:
        logging.error('Error: {0}'.format(e))
        exit()

subreddit = r.subreddit(config['reddit']['subreddit'])

flairs = {}
flair_list = [flair for flair in subreddit.flair()]
# print(f"all unique flairs: {set([flair['flair_text'] for flair in flair_list])}")

for flair in flair_list:
    flairName = flair['flair_text']
    if flairName not in flairs:
        flairs[flairName] = 0
        logging.debug('Flair added: {0}'.format(flairName))
        print('Flair added: {0}'.format(flairName))

    flairs[flairName] += 1
    logging.debug('Flair counted: {0}'.format(flairName))
    #print('Flair counted: {0}'.format(flairName))


logging.info('Sorting flairs...')
sorted_flairs = sorted(flairs.items(), key=lambda x: x[1], reverse=True)
print(f"sorted_flairs: {sorted_flairs}")
logging.info('Writing flairs...')

with io.open(config['output']['filename'], 'w+', encoding='utf-8') as f:
    f.write(str(json.dumps(sorted_flairs, ensure_ascii=False, indent=4, separators=(',', ': '))))

# Write out a CSV copy for easier spreadsheet use
writer = csv.writer(open(config['output']['filenamecsv'], 'w', newline='\n', encoding='utf-8'))
string_list = str(json.dumps(sorted_flairs, ensure_ascii=False, indent=4, separators=(',', ': ')))
statsJson = json.loads(string_list)
for flair, num in statsJson:
    if flair is None:
        flair = 'Null'
    writer.writerow([flair, num])

elapsed_time = str(round(time.time() - start_time, 2))
logging.info('Done!')
logging.info('Completed in {}'.format(elapsed_time))