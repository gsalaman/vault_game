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

The state game is a little more involved.  Let's first talk about how it behaves.
* When the game starts, it lights up a symbol.  Some discussion about wheter this is solid or flashing...flashing tends to attract attention, but then complicates the "success" indications below, so I'm gonna start with solid.
* When you get a symbol right, it'll flash that symbol.  Any OTHER symbols that are correct will stay on.
* Then, when you get all 4, flash that symbol as normal, then flash all 4 fast, then make them solid and open the vault.  Stay here for 5 (TBR) seconds, then go back to either idle or start.

So, for states:
  * Want an idle state where we're doing nothing.  Not really gonna be used for simultaneous, but good for when we do sequential
  * Waiting for input state:  solid symbol, look for button
  * button success state:  you got it right...flash symbol, and turn on any others that you've already got.
  * puzzle success state:  flash all fast, make solid, then open vault.  Here for 5 seconds, then back to either idle or waiting for input.
    

