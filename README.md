# Bach Analysis
a dumb little project, where i compare right and left hand of bach 2part inventions and see how similar they are

## FACTS

contrapunctal music, or at least contrapunctal music in the baroque era, was heavily based (this sentence could end here and still make sense) on
motifs and development of them. fugues are a well-known example of this, where there are multiple voices going through left and right hand, with one
central motif that is first being played by one voice and then it gets variated through in all the different voices.
A fugue usually begins by establishing this motif in what is known as the *exposition*.
The voice first establishing the motif gets the name *Dux* (from latix 'Dux' meaning 'Leader')
and the voices following get the name *Comes* (from Latin 'Comes' meaning 'Companion').

Of course the voices don't stop playing after they finished with the variation of the central motif. usually a different, minor
(minor here in the sense of importance, not in the modal (musical) sense) motif gets played, but this as well gets developed, but not as much.

In your usual fugue, every voice is the Dux at least once (this is not verified, don't cite me on that. its just my experience practicing WTC).
You might ask yourself "huh, i thought dux is only first establishing the motif?". Well, yes. But there is, what in musicology is called, "development".
After exposition there is the development of the theme. **this is the key point to this project**. Every voice gets to be Dux once or twice or whatever,
but what interests me is "how well are Dux and Comes similar to one another", meaning, what is the abstract structure of the piece?

In this project i want to analyse the note distribution, interval distribution and rhythmic distribution
(relative frequency of notes (weighted with their value), intervals and values) along simple polyphonic pieces of music.
My claim is that **the more the piece follows the spirit of couterpoint, the lower the Jensen-Shannon-Divergence between the voices is**,
where i look at the three discussed properties --- or rather *distributions*. The goal is to look at a piece's projected probability distribution
(time independent, the whole piece gets thrown onto one x-axis) and tell how well this fits into the spirit of contrapunctal music.

## Progress

So far i have calculated the Jensen-Shannon divergence for the 15 two-part inventions of JS Bach (1723).
Granted this was only the notes and not the intervals or note values. See *Outlook* for more.
By above line of thought, the most counterpoint-y is Invention 6 in E major (BWV 777).
Invention 13, which i predicted to be first just by going through my copy of the book,
came, to my surprise (i am not very confident), second, which affirms me in the aim of finishing this analysis and maybe getting interesting results
out of it.

## Problems

[The average github user is smart enough that, given they read this whole thing so far,
if i give them exactly this one link, they will understand precisely
what one of my main problems is (timestamp included).](https://youtu.be/FpriHgUyEM0?t=172)

The other main problem is: Bar 34, Prelude 2 in well-tempered clavier, BWV 847. More precisely: what if i have a chord structure in my piece?
what am i supposed to do about the intervals, note values, whatever?

## Outlook

I need to implement the following:

- interval distribution
- value distribution
- avoid parallel voices on consonant intervals
- compare with blatantly non-counterpoint non-baroque era pieces
- (last step) compose a piece which perfectly fits the contrapunctal spirit.

## FAQ
i have yet to get a question about this, that i didn't previously also ask myself.
with that being said, i only really got 3 questions about this so far.
I'm just anticipating new questions, which will *most definitively* get asked (Clueless)

### why?
M C A

### have you talked to musicians about this?
yes

### what did they say?
> "lol"

and

> "oh so its like catholic church music"

### common-practice?
soon<sup>tm</sup>
