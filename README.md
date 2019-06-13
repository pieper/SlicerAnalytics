# SlicerAnalytics
A site and extension for collecting Google Analytics about Slicer usage


## basic proof of concept implementation

- watches for use of modules and reports to google analytics

Issues:

- needs way for users to opt in or out of tracking
(currently don't run it if you don't want to be tracked).

- google analytics isn't really suited for this task so here
we use the utm_ url parameters that typically track different
kinds of advertising campaigns.

- also google analystics is statistical and so we aren't assured
to get all the tracking data we want.

To do a more suitable tracking we need to have a more robust
database that can track the parameters of interest to us, like what
kind of computer is being used, etc.  Maybe we even want to track
things about what type of data they operate on.  To collect this
data we would also need a privacy policy.  Also we would need
to take some steps to be sure people can't abuse the database
for any reason.
