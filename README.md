# MITx_CSIntro_Problems

Problems of the EDX Course in Introduction to Computer Science and Programming Using Python by MITx 6.00.1x
I've decided to make a repository so I can come back to these, reanalyze it and watch my progress.

## Notes on problems:

### MITx_biggestV.py

- With my approach, it turned out to be inconvenient to associate the number of values to the key of the dictionary. Think my code is not really efficient (especially in this section), but it works.

  ```python
  for pair in aDict:
      count = 0
      for item in aDict[pair]:
       count += 1
  ```
