module Main exposing (..)

-- Press buttons to increment and decrement a Counter.
--
-- Read how it works:
--   https://guide.elm-lang.org/architecture/buttons.html
--

import Browser
import Browser.Dom exposing (Element)
import Element
    exposing
        ( Color
        , alignBottom
        , alignRight
        , centerX
        , centerY
        , column
        , el
        , fill
        , fillPortion
        , height
        , layout
        , mouseOver
        , none
        , padding
        , paddingXY
        , paragraph
        , px
        , rgb255
        , row
        , scrollbarY
        , spacing
        , spacingXY
        , table
        , text
        , width
        )
import Element.Background as Background
import Element.Border as Border
import Element.Events exposing (..)
import Element.Font as Font
import Element.Input exposing (button)
import Html exposing (Html)
import Html.Attributes



-- MAIN


main =
    Browser.sandbox { init = init, update = update, view = view }



-- MODEL


type Unit
    = Clove
    | Count
    | Ounce
    | Tablespoon
    | Pound
    | Gram


unitToString : Bool -> Unit -> String
unitToString plural unit =
    case ( unit, plural ) of
        ( Clove, True ) ->
            "Cloves"

        ( Clove, False ) ->
            "Clove"

        ( Count, _ ) ->
            ""

        ( Ounce, True ) ->
            "Oz"

        ( Ounce, False ) ->
            "Oz"

        ( Tablespoon, _ ) ->
            "Tbsp"

        ( Pound, True ) ->
            "lbs"

        ( Pound, False ) ->
            "lb"

        ( Gram, _ ) ->
            "g"


type alias Ingredient =
    { name : String
    , amount : Int
    , unit : Unit
    }


ingredientAmountToString : Ingredient -> String
ingredientAmountToString i =
    String.fromInt i.amount ++ " " ++ unitToString (i.amount > 1) i.unit


ingredientToTable : List Ingredient -> Element.Element msg
ingredientToTable ingredients =
    table
        [ centerX
        , centerY
        , spacing 10
        , padding 10
        ]
        { data = ingredients
        , columns =
            [ { header = text "Name"
              , width = px 400
              , view = \i -> text i.name
              }
            , { header = text "Amount"
              , width = fill
              , view = \i -> text <| ingredientAmountToString i
              }
            ]
        }


type alias Recipe =
    { short_recipe : String
    , author : String
    , ingredients : List Ingredient
    , name : String
    }


chili : Recipe
chili =
    { name = "Chili"
    , short_recipe = """
        Sear meat in large pot. Remove seeds and soak the chiles in warm water. Blend
  tomato, onion, and chiles and add to meat. Add oregano, salt and pepper and cook 
  until meat is tender. Add beans and hominy, cooking for an additional half hour
  or so. 
    """
    , author = "Evan Curtin"
    , ingredients =
        [ { name = "Beef chuck Roast", amount = 2, unit = Pound }
        , { name = "tomato", amount = 32, unit = Ounce }
        , { name = "onion", amount = 1, unit = Count }
        , { name = "garlic", amount = 5, unit = Clove }
        , { name = "poblano chile", amount = 3, unit = Count }
        , { name = "guajillo chile", amount = 4, unit = Count }
        , { name = "ancho chile", amount = 3, unit = Count }
        , { name = "hominy", amount = 32, unit = Ounce }
        , { name = "pinto beans", amount = 32, unit = Ounce }
        , { name = "salt", amount = 1, unit = Tablespoon }
        , { name = "pepper", amount = 1, unit = Tablespoon }
        , { name = "cumin", amount = 1, unit = Tablespoon }
        ]
    }


coffee : Recipe
coffee =
    { name = "Coffee"
    , short_recipe = """
    Pour the things 
    """
    , author = "Evan Curtin"
    , ingredients =
        [ { name = "Coffee", amount = 15, unit = Gram }
        ]
    }


init : Recipe
init =
    chili



-- UPDATE


type RecipeChoice
    = Chili
    | Coffee


recipeChoiceToString : RecipeChoice -> String
recipeChoiceToString msg =
    case msg of
        Chili ->
            "Chili"

        Coffee ->
            "Coffee"


msgToText : RecipeChoice -> Element.Element RecipeChoice
msgToText choice =
    center <| button [ padding 5 ] { onPress = Just choice, label = text <| recipeChoiceToString choice }


update : RecipeChoice -> Recipe -> Recipe
update msg model =
    case msg of
        Chili ->
            chili

        Coffee ->
            coffee



-- VIEW


blankSideBar =
    [ height fill
    , width <| fillPortion 1
    , Background.color <| rgb255 92 99 118
    , Font.color <| rgb255 255 255 255
    ]


sideBar : Element.Element RecipeChoice
sideBar =
    column blankSideBar <|
        [ text "Recipes" ]
            ++ List.map
                msgToText
                [ Coffee, Chili ]


type Palette
    = Red
    | Blue


toColor : Palette -> Color
toColor pal =
    case pal of
        Red ->
            rgb255 50 50 250

        Blue ->
            rgb255 200 200 200


center : Element.Element msg -> Element.Element msg
center element =
    el
        [ Element.htmlAttribute (Html.Attributes.style "marginLeft" "auto")
        , Element.htmlAttribute (Html.Attributes.style "marginRight" "auto")
        ]
        element


centerAll : List (Element.Element msg) -> List (Element.Element msg)
centerAll elements =
    List.map
        center
        elements


recipePanel : Recipe -> Element.Element msg
recipePanel recipe =
    let
        header =
            row
                [ width fill
                , paddingXY 20 5
                , Border.color <| rgb255 200 200 200
                ]
                [ el [] <| text recipe.name ]
    in
    column [ height fill, width <| fillPortion 5 ] <|
        centerAll
            [ header
            , text recipe.short_recipe
            , ingredientToTable recipe.ingredients
            ]


view : Recipe -> Html RecipeChoice
view recipe =
    layout
        [ Font.color (rgb255 255 100 100)
        , Font.size 18
        , Font.family
            [ Font.external
                { url = "https://fonts.googleapis.com/css?family=EB+Garamond"
                , name = "Lato"
                }
            , Font.sansSerif
            ]
        ]
    <|
        row [ height fill, width fill ]
            [ sideBar
            , recipePanel recipe
            , column blankSideBar []
            ]
