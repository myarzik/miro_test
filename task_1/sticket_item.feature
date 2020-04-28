Feature: testing of the Sticky note
  scenarios for testing multi-user board with sticky note
  Background:
    Given user "Anton"
    And user "Roman"
    And user "Anton" working on the "board_1"
    And user "Roman" working on the "board_1"

  Scenario Outline: testing of adding and deleting stickers
    When "Roman" adding the new sticker with text "kekeke" and <color> on the "board_1"
    Examples:
    |  color  |
    | color1  |
    | color2  |
    | color3  |
    | color4  |
    | color5  |
    | color6  |
    | color7  |
    | color8  |
    | color9  |
    | color10 |
    | color11 |
    | color12 |

    Then "Roman" can see this sticker
    And "Anton" can see this sticker

    When "Anton" adding the bulk of 12 new stickers with different texts and different colors on the "board_1"
    Then "Anton" can see this bulk of stickers
    And "Roman" can see this bulk of stickers

    When "Anton" press "undo"
    Then "Anton" can see that this bulk of stickers disappears
    And "Roman" can see that this bulk of stickers disappears

    When "Roman" deletes sticker the with text "kekeke"
    Then "Roman" can see that this bulk of stickers disappears
    And "Anton" can see that this bulk of stickers disappears


  Scenario: testing of stickers editing
    When "Roman" adding the new sticker with text "ololo" on the "board_1"
    Then "Roman" can see this sticker
    And "Anton" can see this sticker

    When "Roman" moves this sticker to another position
    Then "Roman" can see that this sticker moves
    And "Anton" can see that this sticker moves

    When "Anton" lock this sticker
    Then "Roman" can't edit this sticker
    And "Anton" can unlock this sticker

    When "Anton" unlock this sticker
    Then "Roman" can edit this sticker
    And "Anton" can edit this sticker

    When "Anton" copy this sticker
    Then "Anton" can see that this sticker moves
    And "Roman" can see the copy of this sticker


  Scenario Outline: testing of editing sticker content
    When "Roman" adding the new sticker with text "ololo" on the "board_1"
    Then "Roman" can see this sticker
    And "Anton" can see this sticker

    When "Roman" changes the <content> of this sticker
    Examples:
    | parameter |
    | form      |
    | size      |
    | color     |
    | tag       |
    | assignee  |
    | link      |
    | date      |
    | parameter |
    | parameter |
    Then "Roman" can see this changes
    And "Anton" can see this changes
