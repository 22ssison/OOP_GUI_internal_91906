"""
NCEA Level 3 Chemistry Quiz: Properties of Organic Compounds
------------------------------------------------------------
An interactive GUI application developed using Tkinter and OOP principles.
This program evaluates knowledge of organic functional groups and reactions 9
through a dynamic multiple-choice interface.
"""

from tkinter import *
from tkinter import messagebox

class Question:
    """"""
    def __init__(self, text, options, ans_index, marks):
        """"""
        self.text = text # question
        self.options = options # different options in list
        self.ans_index = ans_index # index of correct answer
        self.marks = marks # how many marks the question is worth

class OrgQuiz:
    """"""
    def __init__(self, parent):
        """"""
        self.parent = parent
        self.questions = [ 
            Question("What is the correct IUPAC name for: CH3CH=CHCH3?", ["but-1-ene", "but-2-ene", "2-butene", "propene", "1-butene"], 1, 1),
            Question("Which functional group is present in 3-chloropentane?", ["Alcohol", "Amine", "Alkene", "Haloalkane", "Ketone"], 3, 1),
            Question("What is the IUPAC name for CH3CH2NH2?", ["Methanamine", "Ethanamine", "Propanamine", "Methylamine", "Aminoethane"], 1, 1),
            Question("Which of the following is the general formula for an aldehyde?", ["R-OH", "R-NH2", "R-CHO", "R-COOH", "R-COR'"], 2, 1),
            Question("The IUPAC name for CH3COCH3 is:", ["Propanal", "Propanone", "Butanone", "2-propanone", "Acetone"], 1, 1),
            Question("Which of the following molecules contains a chiral carbon atom?", ["CH3CH2CH2OH", "CH3CH(OH)CH3", "CH3CH(OH)CH2CH3", "CH3COCH3", "CH2=CH2"], 2, 2),
            Question("Enantiomers are stereoisomers that are:", ["Non-superimposable mirror images", "Superimposable mirror images", "Geometric isomers", "Constitutional isomers", "Conformational isomers"], 0, 1),
            Question("A key property of enantiomers is that they:", ["Have different melting points", "Have different boiling points", "Rotate light in same direction", "Rotate light in opposite directions", "Have different chemical properties"], 3, 1),
            Question("Primary reason for using reflux in organic reactions?", ["Increase rate by cooling", "Prevent loss of volatiles", "Ensure room temp", "Easy separation", "Increase solubility"], 1, 1),
            Question("Distillation is primarily used for:", ["Mixing reactants", "Constant heating", "Separating liquids by boiling point", "Cooling reactions", "Increasing surface area"], 2, 1),
            Question("Why are alkanes insoluble in water?", ["Form hydrogen bonds", "They are polar", "Non-polar; cannot interact with water", "React with water", "High melting points"], 2, 2),
            Question("Which functional group can form hydrogen bonds?", ["Alkene", "Haloalkane", "Amine", "Alkane", "Ketone"], 2, 1),
            Question("Effect of -OH group on boiling point vs similar alkane?", ["Decreases it", "Increases it via hydrogen bonding", "No effexct", "Depends on weight", "Only increases for primary"], 1, 2),
            Question("Smaller amines (up to C5) are soluble because:", ["Non-polar", "Ionic bonds", "Polar amino group forms H-bonds", "React to form non-polar", "Low molecular weight"], 2, 1),
            Question("As carbon chain length increases in alcohols, solubility:", ["Increases (Van der Waals)", "Decreases (Non-polar part grows)", "Remains constant", "Depends on OH position", "Increases (H-bonding)"], 1, 2),
            Question("Alkenes are characterised by:", ["Single C-C bond", "C-halogen bond", "Carbonyl group", "Carbon-carbon double bond", "C-N bond"], 3, 1),
            Question("Characteristic reaction type for Alkenes?", ["Substitution", "Elimination", "Addition", "Condensation", "Hydrolysis"], 2, 2),
            Question("Test for unsaturation involves decolourisation of:", ["K2Cr2O7", "Tollens'", "Fehling's", "Bromine water", "KMnO4"], 3, 1),
            Question("Haloalkanes + aqueous OH- produces:", ["Alkenes", "Alcohols", "Amines", "Aldehydes", "Carboxylic acids"], 1, 1),
            Question("Elimination of haloalkanes is favoured by:", ["Aqueous NaOH", "Conc. HCl", "KOH in alcohol", "Conc. H2SO4", "H2O/H+"], 2, 2),
            Question("Amines are basic because they:", ["Donate a proton", "Accept a proton", "Donate electron pair", "Oxidise readily", "Form non-polar solutions"], 1, 1),
            Question("Reaction of an amine with an acid forms a:", ["Carboxylic acid", "Salt", "Alcohol", "Aldehyde", "Ketone"], 1, 2),
            Question("Primary alcohols can be oxidised to:", ["Ketones", "Aldehydes only", "Carboxylic acids only", "Aldehydes then Carboxylic acids", "No reaction"], 3, 1),
            Question("Colour change for K2Cr2O7/H+ during alcohol oxidation?", ["Colourless to purple", "Purple to colourless", "Orange to green", "Green to orange", "Blue to red"], 2, 2),
            Question("Secondary alcohols are oxidised to:", ["Aldehydes", "Carboxylic acids", "Ketones", "Primary alcohols", "No reaction"], 2, 1),
            Question("Tertiary alcohols:", ["Oxidise to ketones", "Oxidise to acids", "Oxidise to aldehydes", "Do not readily oxidise", "Eliminate to alkenes"], 3, 1),
            Question("Propan-1-ol + K2Cr2O7/H+ under reflux produces:", ["Propanal", "Propanone", "Propanoic acid", "CO2", "No reaction"], 2, 2),
            Question("Aldehydes oxidise to carboxylic acids using:", ["NaBH4", "H2SO4", "Tollens' reagent", "KOH", "H2/catalyst"], 2, 1),
            Question("Positive result for Aldehyde + Tollens'?", ["Red ppt", "Silver mirror", "Green solution", "Bubbles", "No change"], 1, 2),
            Question("Ketones reduced by NaBH4 form:", ["Primary alcohols", "Secondary alcohols", "Aldehydes", "Carboxylic acids", "No reaction"], 1, 1),
            Question("Which contains a carbonyl group (C=O)?", ["Alcohol", "Amine", "Alkene", "Aldehyde", "Haloalkane"], 3, 1),
            Question("Tollens' reagent distinguishes Aldehydes/Ketones because:", ["Both react at different rates", "Aldehydes react, Ketones don't", "Ketones react, Aldehydes don't", "Aldehydes produce black ppt", "Ketones change color"], 1, 2),
            Question("Alkene + Bromine water is what reaction type?", ["Substitution", "Elimination", "Addition", "Oxidation", "Reduction"], 2, 1),
            Question("2-bromopropane + ethanolic KOH produces:", ["Propan-1-ol", "Propan-2-ol", "Propane", "Propene", "1,2-dibromopropane"], 3, 2),
            Question("Amines contain which element?", ["Oxygen", "Halogen", "Nitrogen", "Carbonyl", "Hydroxyl"], 2, 1),
            Question("Short-chain amine + HCl, solubility:", ["Decreases (less polar)", "Decreases (covalent)", "Increases (ionic salt)", "Same", "Insoluble"], 2, 2),
            Question("Functional group for alcohols is:", ["-CHO", "-COOH", "-OH", "-NH2", "-C=C-"], 2, 1),
            Question("What type of alcohol is propan-2-ol?", ["Primary", "Secondary", "Tertiary", "Methanol", "Phenol"], 1, 2),
            Question("Dehydration of an alcohol involves heating with:", ["Aqueous NaOH", "KMnO4", "Conc. H2SO4", "Tollens'", "NaBH4"], 2, 1),
            Question("Ethanol elimination produces:", ["Ethanal", "Ethanoic acid", "Ethene", "Ethane", "Diethyl ether"], 2, 2),
            Question("Aldehyde functional group position:", ["Middle", "End", "Any carbon", "Second carbon", "Attached to ring"], 1, 1),
            Question("Propanal + K2Cr2O7/H+ produces:", ["Propan-1-ol", "Propan-2-ol", "Propanoic acid", "Propanone", "No reaction"], 2, 2),
            Question("Ketones have the carbonyl group bonded to:", ["One Hydrogen", "Two Hydrogens", "Two Carbons", "One C and One H", "One Nitrogen"], 2, 1),
            Question("Reactivity of Ketones towards oxidation:", ["Oxidise to aldehydes", "Oxidise to acids", "React with Tollens'", "Resistant to common oxidants", "Oxidise to primary alcohols"], 3, 2),
            Question("Shape around C=C bond in alkenes:", ["Tetrahedral", "Trigonal planar", "Linear", "Bent", "Pyramidal"], 1, 1),
            Question("Which haloalkane eliminates easiest with alcoholic KOH?", ["CH3CH2Cl", "CH3CH2CH2Br", "CH3CH(Br)CH3", "(CH3)3CCl", "CH3Cl"], 3, 2),
            Question("Type of isomerism in but-2-ene:", ["Constitutional", "Stereoisomerism", "Optical", "Geometric (cis-trans)", "Structural"], 3, 1),
            Question("Best way to distinguish pentan-1-ol and pentan-2-one?", ["Solubility", "Boiling point", "K2Cr2O7 reaction", "Density", "Formula"], 2, 2),
            Question("Haloalkane + conc. NH3 produces:", ["Alcohol", "Amine", "Carboxylic acid", "Aldehyde", "Ketone"], 1, 1),
            Question("Effect of increasing IMF strength on boiling point:", ["Weaker leads to higher", "Stronger leads to lower", "Stronger needs more energy; higher BP", "No effect", "Depends on size only"], 2, 2)
        ]

        # Initial (default) statuses
        self.score = 0 
        self.question_index = 0 
        self.total_questions_to_answer = 0  # will be set by the user at entry
        self.user_choice = IntVar()  # track which rb clicked
        self.user_choice.set(-1)     # since 0 is 1st value in radiobutton, use -1 and start w/ nothing selected.

        # 1) Start Screen
        self.start_frame = Frame(parent)
        self.start_frame.grid(row=0, column=0)

        # Title + Instructions
        Label(self.start_frame, text="NCEA Level 3 Organic Chemistry").grid()
        self.instruction_label = Label(self.start_frame, text="Welcome! This quiz covers functional groups, isomerism, and organic reactions.50 questions available. Select your desired quiz length below. Note: Questions vary between 1 and 2 marks each.").grid()
        
        Label(self.start_frame, text="Num of Questions:").grid(row=0, column=0, padx=10, pady=5)
        self.num_questions_entry = Entry(self.start_frame)
        self.num_questions_entry.grid(row=0, column=1, padx=10, pady=5)

        self.start_button = Button(self.start_frame, text="Start Quiz", command=validate_start.previous)

        # 2) Quiz Screen
        self.quiz_frame = Frame(parent)
        # don't .grid() yet; validate_start will do that.

        # Question text
        self.question_label = Label(self.quiz_frame, text="", font=("Arial", 12), wraplength=400)
        self.question_label.pack(pady=10)

        # Radio Buttons - creates list of 5 ans
        self.rb_list = []
        for i in range(5):
            rb = Radiobutton(self.quiz_frame, text="", variable=self.user_choice, value=i) # follows index of each ans
            rb.pack(anchor=W) # vertically + west side of screen 
            self.rb_list.append(rb)

        # Control Buttons
        self.next_button = Button(self.quiz_frame, text="Next Question", command=self.next_question)
        self.next_button.pack(side=LEFT, padx=10)

        self.skip_button = Button(self.quiz_frame, text="Skip", command=self.skip_question)
        self.skip_button.pack(side=LEFT, padx=10)
        
        self.reset_button = Button(self.quiz_frame, text="Reset Quiz", command=self.reset_quiz)
        self.reset_button.pack(side=LEFT, padx=10)

        # 3) Results Screen
        self.results_frame = Frame(parent)
        # don't .grid() yet; validate_results will do that.

        self.results_label = Label(self.quiz_frame, text="Quiz Completed!", font=("Arial", 24, "bold"), fg="#2C3E50"
        )
        self.results_label.pack(pady=20)

        # Score display - placeholder for score atm
        self.score_label = Label(self.quiz_frame, text="Your Score: --/--", font=("Arial", 18))
        self.score_label.pack(pady=10)

        # restart/quit
        self.restart_btn = Button(self.quiz_frame, text="Try Again", width=15)
        self.restart_btn.pack(side=LEFT, padx=10, pady=20)

        self.quit_btn = Button(self.quiz_frame, text="Exit", width=15, command=self.root.quit)
        self.quit_btn.pack(side=RIGHT, padx=10, pady=20)
        
    def validate_start(self):
        """validates a valid # of questions before allowing quiz to begin."""
        try:
            num = int(self.num_questions_entry.get()) 
            if 1 <= num <= len(self.questions): # if num is sensible based on length of list
                self.total_questions_to_answer = num 
                self.start_frame.grid_forget()
                self.quiz_frame.grid(row=0, column=0)
                self.update_quiz() # Show the first question
            else:
                messagebox.showwarning("Error", "Please enter between 1 and 50.")
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid number.")
    
    def update_quiz(self):
        self.user_choice.set(x-1) # rb nothing selected

        current_question = self.questions[self.question_index] # get first element - object - in q list

        self.question_label.config(
            text=f"Question {self.question_index + 1} of {self.total_questions_to_answer}\n\n{current_queston.text}"
        )
        
        for i in range(5): 
            self.rb_list[i].config(text=current_question.options[i]) # update text shown for each rb
            # current_question.options list of 5 possible answers
    
    def next_question(self):
        choice = self.user_choice.get() 
        
        if choice == -1:
            messagebox.showwarning("No Selection. Please select an answer before moving on.")
            return # Stop the function here so they have to pick something

        # add score to selected ans to current q
        current_question = self.questions[self.question_index] # gets the object in the q list.
        if choice == current_question.ans_index: # compares index selected to correct ans
            self.score += current_question.marks # add score
        
        # move to next q
        self.question_index += 1
        
        if self.question_index < self.total_questions_to_answer: # checks if still qs to ans - based on user's desired length of quiz
            self.update_quiz()
        else:
            self.show_results()

        def show_results(self):
            self.quiz_frame.grid_forget()
            self.results_frame.grid(row=0, column=0)
            
            # Calc max possible score for questions answered based on user's desired length of quiz. Also consider different questions are worth different points. 
            max_score = sum(question.marks for question in self.questions[:self.total_questions_to_answer])
            
            # Percentage Score
            percentage = (self.score / max_score) * 100
            
            # update labels
            self.results_label.config(text="Quiz Completed!")
            self.score_label.config(
                text=f"Score: {self.score} / {max_score}\nPercentage: {round(percentage)}%"
        )

        def show_results(self):
            self.quiz_frame.grid_forget()
            self.results_frame.grid(row=0, column=0)
            
            max_score = 0
            
            # get specific list of questions user actually answered
            played_questions = self.questions[:self.total_qs_to_answer]
            
            # add all specific question marks
            for question in played_questions:
                max_score += question.marks
                
            # Percentage
            percentage = (self.score / max_score) * 100
            
            self.results_label.config(text="Quiz Completed!")
            self.score_label.config(
                text=f"Score: {self.score} / {max_score}\nPercentage: {round(percentage)}%"
            )