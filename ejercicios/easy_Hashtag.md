# Hash, Hash, Hashtag - Easy

## Summary
In this problem your job is to identify the most popular hashtags
appearing in a set of posts. The input will consist of a list of posts with
their respective timestamp. Each post will be expressed in 2 lines of input -
the first line will consist of a timestamp of the post - an integer from [0,
1440) identifying the minute of the day in which the post appeared online
followed by a line that will consist of the post's content - a space-delimited
line of text. A hashtag is defined as any token which begins with a # after an
empty space.

## Problem
Which hashtag appears most often across all posts? Your output should
consist of a single line consisting of the hashtag in question.

### Example 1

#### Input
```
80
This #post has hashtag #b 5 times, #b #b #b #b

0
This is a #post

60
This #post has hashtags #a #b and #c

220
This is for the time #window

200
This #post again has hashtag #b 3 times #b #b but happens in a time #window

210
This #post is for the time #window

220
This is for the time #window

240
Now in this time #window people like talking about windows

20
This is another #post where I say how #happy I am
```

#### Output
In the example input, *#b* is the most common hashtag in all posts. It appears 9
times in total.

```
#b
```
