This code will take an input after starting, and begin downloading every image found under that

Needed:
- Take input to a search term
- go to imgur.com/search?q=''

- Find all images
  - Select all <img> tags
    - take href, go to gallery pages

- Download them
  - find <.post-image img> (videos will be skipped)
    - take the src if it exists
    - save it with the alt as the file title
