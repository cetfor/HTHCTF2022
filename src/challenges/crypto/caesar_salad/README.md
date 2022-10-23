## Description
This challenge is a progressive caesar cipher that also contains a timing oracle. When submitting a flag of adequate length, the challenge will stall for one second per correct character. This simulates a timing side channel attack where the time it takes the system to process a correct character is noticably longer than to process an incorrect character.

Using this oracle, a user can incramentally build the correct solution by timing their submissions to the server. For example, the user knows all flags have the same format of `hth{<flag_here>}`. So they can sumbit:

```
hth{aaaaaaaaaaaaaaaaaaaa}   # 4.3 seconds
hth{baaaaaaaaaaaaaaaaaaa}   # 4.1 seconds (.2 second delta)
hth{caaaaaaaaaaaaaaaaaaa}   # 4.6 seconds (.5 second delta)
hth{daaaaaaaaaaaaaaaaaaa}   # 4.2 seconds (.4 second delta)
...
hth{paaaaaaaaaaaaaaaaaaa}   # 5.3 seconds (1.1 second delta!)
```

If they continue this way, each correct letter will cause the system to leak timing data that tells them they have a new correct letter.  Even if they completely miss the oracle, they can solve this challenge by realizing the use of a caesar cipher where the shift increments with each character position, a progressive caesar cipher.

## Running this challenge
```
$ docker-compose build
$ docker-compose up
$ nc 127.0.0.1 22201
```
