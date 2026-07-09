# Vault Game

My random notes:

If I do sequential-style, I don't need to worry about the "blocking" waits.  Can still do states:

* Waiting for key_button press
* Indicating key success (spin wheel)
* Vault symbol 1 - solid
* Flash on success
* (repeat for all symbols)
* Open door
* Wait (10?) seconds, then do it all over again.

If I go simultaneous, I really need two state machines....one for the key, one for the shape puzzle.

The key one is most straighforward:
* Waiting for press
* Spin ring.  Has a count (40), and then a "next update time" + 50 ms
* Flash ring.  Has a count (6), and then a "next update time" + 200 ms
* Then back to "waiting for press.

The state game is a little more involved:
  * Want an idle state where we're doing nothing.  Not really gonna be used for simultaneous, but good for when we do sequential
  * Waiting for input state:  flash symbol, look for button
  * button success state:  you got it right...flash all
  * puzzle success state:  flash all again?  Faster?  Open vault.  Here for 5 seconds, then back to either idle or waiting for input.
    

