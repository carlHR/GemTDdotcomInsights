code0 = '''
    <div class="vbox">
        <div class="stretch"></div>
        <div class="hbox">
            <div class="vbox">
                <div class="stretch"></div>
                <div class="recipe-name">%s</div>
                <div class="stretch"></div>
            </div>
            <div class="space8"></div>
            <div class="vbox">
                <img title="%s" class="gem-larger" src="%s">
            </div>

            <div class="space8"></div>
            <div class="vbox">
                <div class="stretch"></div>
                =
                <div class="stretch"></div>
            </div>
            <div class="space8"></div>

            <div class="vbox">
                <div class="stretch"></div>
                <img title="%s" src="%s">
                <div class="stretch"></div>
            </div>

            <div class="space8"></div>
            <div class="vbox">
                <div class="stretch"></div>
                +
                <div class="stretch"></div>
            </div>
            <div class="space8"></div>

            <div class="vbox">
                <div class="stretch"></div>
                <div class="hbox">
                    <div class="vbox">
                        <div class="stretch"></div>
                        <img title="%s" src="%s">
                        <div class="stretch"></div>
                    </div>

                    <div class="space8"></div>

                    <div class="vbox">
                        <div class="stretch"></div>
                        |
                        <div class="stretch"></div>
                    </div>

                    <div class="space8"></div>

                    <div class="vbox">
                        <div class="stretch"></div>
                        <img title="%s" src="%s">
                        <div class="stretch"></div>
                    </div>
                </div>
                <div class="stretch"></div>
            </div>
        </div>
        <div class="stretch"></div>
    </div>'''

code1 = '''
    <div class="vbox">
        <div class="stretch"></div>
        <div class="hbox">
            <div class="vbox">
                <div class="stretch"></div>
                <div class="recipe-name">%s</div>
                <div class="stretch"></div>
            </div>
            <div class="space8"></div>
            <div class="vbox">
                <img title="%s" class="gem-larger" src="%s">
            </div>

            <div class="space8"></div>
            <div class="vbox">
                <div class="stretch"></div>
                =
                <div class="stretch"></div>
            </div>
            <div class="space8"></div>

            <div class="vbox">
                <div class="stretch"></div>
                <img title="%s" src="%s">
                <div class="stretch"></div>
            </div>

            <div class="space8"></div>
            <div class="vbox">
                <div class="stretch"></div>
                +
                <div class="stretch"></div>
            </div>
            <div class="space8"></div>

            <div class="vbox">
                <div class="stretch"></div>
                <div class="hbox">
                    <div class="vbox">
                        <div class="stretch"></div>
                        <img title="%s" src="%s">
                        <div class="stretch"></div>
                    </div>

                    <div class="space8"></div>

                    <div class="vbox">
                        <div class="stretch"></div>
                        |
                        <div class="stretch"></div>
                    </div>

                    <div class="space8"></div>

                    <div class="vbox">
                        <div class="stretch"></div>
                        <img title="%s" src="%s">
                        <div class="stretch"></div>
                    </div>

                    <div class="space8"></div>

                    <div class="vbox">
                        <div class="stretch"></div>
                        |
                        <div class="stretch"></div>
                    </div>

                    <div class="space8"></div>

                    <div class="vbox">
                        <div class="stretch"></div>
                        <img title="%s" src="%s">
                        <div class="stretch"></div>
                    </div>
                </div>
                <div class="stretch"></div>
            </div>
        </div>
        <div class="stretch"></div>
    </div>'''

ls = [
	["Hold:", "Hold",      "https://www.gemtowerdefense.com/assets/holdslate.png", "Normal Topaz", "https://www.gemtowerdefense.com/assets/normaltopaz.png",             "Flawed Amethyst", "https://www.gemtowerdefense.com/assets/flawedamethyst.png", "Flawed Sapphire", "https://www.gemtowerdefense.com/assets/flawedsapphire.png"],
	["Air:", "Air",       "https://www.gemtowerdefense.com/assets/airslate.png", "Normal Amethyst", "https://www.gemtowerdefense.com/assets/normalamethyst.png",         "Flawed Emerald", "https://www.gemtowerdefense.com/assets/flawedemerald.png", "Flawed Opal", "https://www.gemtowerdefense.com/assets/flawedopal.png", "Flawed Ruby", "https://www.gemtowerdefense.com/assets/flawedruby.png"],
	["Opal Vein:", "Opal Vein", "https://www.gemtowerdefense.com/assets/opalveinslate.png", "Normal Opal", "https://www.gemtowerdefense.com/assets/normalopal.png",      "Flawed Ruby", "https://www.gemtowerdefense.com/assets/flawedruby.png", "Flawed Topaz", "https://www.gemtowerdefense.com/assets/flawedtopaz.png"],
	["Slow:", "Slow",      "https://www.gemtowerdefense.com/assets/slowslate.png", "Normal Sapphire", "https://www.gemtowerdefense.com/assets/normalsapphire.png",       "Flawed Aquamarine", "https://www.gemtowerdefense.com/assets/flawedaquamarine.png", "Flawed Diamond", "https://www.gemtowerdefense.com/assets/flaweddiamond.png", "Flawed Emerald", "https://www.gemtowerdefense.com/assets/flawedemerald.png"],
	["Spell:", "Spell",     "https://www.gemtowerdefense.com/assets/spellslate.png", "Normal Aquamarine", "https://www.gemtowerdefense.com/assets/normalaquamarine.png", "Flawed Amethyst", "https://www.gemtowerdefense.com/assets/flawedamethyst.png", "Flawed Diamond", "https://www.gemtowerdefense.com/assets/flaweddiamond.png"],
	["Poison:", "Poison",    "https://www.gemtowerdefense.com/assets/poisonslate.png", "Normal Emerald", "https://www.gemtowerdefense.com/assets/normalemerald.png",     "Flawed Aquamarine", "https://www.gemtowerdefense.com/assets/flawedaquamarine.png", "Flawed Opal", "https://www.gemtowerdefense.com/assets/flawedopal.png", "Flawed Topaz", "https://www.gemtowerdefense.com/assets/flawedtopaz.png"],
	["Damage:", "Damage",    "https://www.gemtowerdefense.com/assets/damageslate.png", "Normal Diamond", "https://www.gemtowerdefense.com/assets/normaldiamond.png",     "Flawed Opal", "https://www.gemtowerdefense.com/assets/flawedopal.png", "Flawed Sapphire", "https://www.gemtowerdefense.com/assets/flawedsapphire.png"],
	["Range:", "Range",     "https://www.gemtowerdefense.com/assets/rangeslate.png", "Normal Ruby", "https://www.gemtowerdefense.com/assets/normalruby.png",             "Flawed Amethyst", "https://www.gemtowerdefense.com/assets/flawedamethyst.png", "Flawed Ruby", "https://www.gemtowerdefense.com/assets/flawedruby.png", "Flawed Topaz", "https://www.gemtowerdefense.com/assets/flawedtopaz.png"],
]

output = ''
for i, v in enumerate(ls):
	if (len(v) == 11):
		output += code1 % (v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10])
	else:
		output += code0 % (v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8])

	output += '\n    <div class="space8"></div>\n'

print(output)
