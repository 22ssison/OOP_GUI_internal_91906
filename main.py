"""
NCEA Level 3 Chemistry Quiz: Properties of Organic Compounds.
------------------------------------------------------------
An interactive GUI application developed using Tkinter and OOP principles.
This program evaluates knowledge of organic functional groups and reactions
through a dynamic multiple-choice interface.
"""

from tkinter import *
from tkinter import messagebox
import random


class Question:
    """Represents a quiz question with its options, answer, and mark value."""

    def __init__(self, text, options, ans_index, marks):
        """Initialize the question with text, options list, and answer index."""
        self.text = text  # The question prompt.
        self.options = options  # List of 5 possible answers.
        self.ans_index = ans_index  # The index of the correct answer.
        self.marks = marks  # Marks awarded for a correct answer.


class OrgQuiz:
    """The main application class for the Organic Chemistry Quiz."""

    def __init__(self, parent):
        """Initialize the GUI and define the database of 50 questions."""
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

        # Tracking status variables.
        self.score = 0 
        self.question_index = 0 
        self.total_questions_to_answer = 0
        self.user_choice = IntVar() 
        self.user_choice.set(-1)

        # 1) Start Screen Setup.
        self.start_frame = Frame(parent)
        self.start_frame.grid(row=0, column=0)

        Label(self.start_frame, text="NCEA Level 3 Organic Chemistry").grid()
        self.instruction_label = Label(
            self.start_frame, 
            text="Welcome! This quiz covers functional groups, isomerism, and reactions.",
            wraplength=400
        )
        self.instruction_label.grid()

        Label(self.start_frame, text="Num of Questions:").grid()
        self.num_questions_entry = Entry(self.start_frame)
        self.num_questions_entry.grid()

        self.start_button = Button(
            self.start_frame, text="Start Quiz", command=self.validate_start
        )
        self.start_button.grid()

        # 2) Quiz Screen Setup.
        self.quiz_frame = Frame(parent)

        self.question_label = Label(
            self.quiz_frame, text="", font=("Arial", 12), wraplength=400
        )
        self.question_label.pack(pady=10)

        self.rb_list = []
        for i in range(5):
            rb = Radiobutton(
                self.quiz_frame, text="", variable=self.user_choice, value=i
            )
            rb.pack(anchor=W)
            self.rb_list.append(rb)

        self.next_button = Button(
            self.quiz_frame, text="Next Question", command=self.next_question
        )
        self.next_button.pack(side=LEFT, padx=10, pady=10)

        self.skip_button = Button(
            self.quiz_frame, text="Skip", command=self.skip_question
        )
        self.skip_button.pack(side=LEFT, padx=10, pady=10)

        # 3) Results Screen Setup.
        self.results_frame = Frame(parent)

        self.results_label = Label(
            self.results_frame, text="Quiz Completed!", 
            font=("Arial", 24, "bold"), fg="#2C3E50"
        )
        self.results_label.pack(pady=20)

        self.score_label = Label(
            self.results_frame, text="Your Score: --/--", font=("Arial", 18)
        )
        self.score_label.pack(pady=10)

        self.restart_btn = Button(
            self.results_frame, text="Try Again", width=15, command=self.reset_quiz
        )
        self.restart_btn.pack(side=LEFT, padx=10, pady=20)

        self.quit_btn = Button(
            self.results_frame, text="Exit", width=15, command=self.confirm_exit
        )
        self.quit_btn.pack(side=RIGHT, padx=10, pady=20)

        self.selected_questions = []
        
    def validate_start(self):
        """Validate input count and transition to the quiz screen."""
        try:
            num = int(self.num_questions_entry.get()) 
            if 1 <= num <= len(self.questions):
                self.total_questions_to_answer = num
                self.selected_questions = random.sample(self.questions, num)
                self.start_frame.grid_forget()
                self.quiz_frame.grid(row=0, column=0)
                self.update_quiz()
            else:
                messagebox.showwarning("Error", "Please enter between 1 and 50.")
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid number.")
    
    def update_quiz(self):
        """Update the quiz frame with the current question data."""
        self.user_choice.set(-1)
        current_question = self.selected_questions[self.question_index]

        self.question_label.config(
            text=f"Question {self.question_index + 1} of "
                 f"{self.total_questions_to_answer}\n\n{current_question.text}"
        )
        
        for i, option in enumerate(current_question.options):
            if i < len(self.rb_list):
                self.rb_list[i].config(text=option)

    def next_question(self):
        """Process the user's answer and move to the next question."""
        choice = self.user_choice.get()
        
        if choice == -1:
            messagebox.showwarning(
                "No Selection", "Please choose an answer first."
            )
            return

        current_question = self.selected_questions[self.question_index]
        if choice == current_question.ans_index:
            self.score += current_question.marks
            
        self.question_index += 1
        
        if self.question_index < self.total_questions_to_answer:
            self.update_quiz()
        else:
            self.show_results()

    def reset_quiz(self):
        """Wipe scores and return the user to the start screen."""
        self.score = 0
        self.question_index = 0
        self.total_questions_to_answer = 0
        self.user_choice.set(-1)

        self.results_frame.grid_forget()
        self.quiz_frame.grid_forget()
        self.start_frame.grid(row=0, column=0)

        self.num_questions_entry.delete(0, END)
    
    def confirm_exit(self):
        """Close the program after user confirmation."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.parent.destroy()

    def skip_question(self):
        """Move to next question without awarding marks."""
        if messagebox.askyesno("Skip", "Skip? No marks will be awarded."):
            self.question_index += 1
            if self.question_index >= self.total_questions_to_answer:
                self.show_results()
            else:
                self.update_quiz()

    def show_results(self):
        """Display the final summary and calculate percentage."""
        self.quiz_frame.grid_forget()
        self.results_frame.grid(row=0, column=0)
    
        max_possible = sum(q.marks for q in self.selected_questions)
        percentage = (self.score / max_possible * 100) if max_possible > 0 else 0
        
        self.score_label.config(
            text=f"Score: {self.score} / {max_possible}\n"
                 f"Percentage: {round(percentage)}%"
        )


if __name__ == "__main__":
    root = Tk()
    root.title("Organic Chemistry Quiz")
    app = OrgQuiz(root)
    root.mainloop()