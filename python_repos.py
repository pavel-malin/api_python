import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Create an API call and save the response.
url = 'https://api.github.com/search/repositories?q=language:Python&sort= \
       stars' # q=language:C, Ruby, Java, Perl, Haskell....
r = requests.get(url)
print("Status code:", r.status_code)

# Save API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Analysis of repository.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

# Get a desciption of the project (if availble).
    description = repo_dict['description']
    if not description:
        description = "No description provided."
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)


# Build visualization.
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style) # x_label_rotation=45,
                                             # show_legend=False
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

'''
# Analysis of repository.
print("Respositories returned:", len(repo_dicts))
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

# Analysis of the first repository.
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# Inforamtion on the most popular repository in github
# and all the information on it.
print("\nSelected inforamtion about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
'''
