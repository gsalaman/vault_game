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


