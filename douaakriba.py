import tkinter as tk
from tkinter import messagebox, ttk
from experta import *

# Define the expert system knowledge base with logical operators
class ComputerDiagnosis(KnowledgeEngine):
    @DefFacts()
    def initialize(self):
        yield Fact(action="diagnose")

    @Rule(Fact(action="diagnose"),
      Fact(symptom="computer_does_not_start"),
      OR(Fact(symptom="no_fan"), Fact(symptom="no_led")))
    def power_supply_failure_v2(self):
      self.declare(Fact(diagnosis="Power Supply Failure", recommendation="Check or replace the power supply."))

   
    @Rule(Fact(action="diagnose"),
          Fact(symptom="random_crashes"),
        OR( Fact(symptom="blue_screen"), Fact(symptom="beeps")))
    def ram_failure(self):
        self.declare(Fact(diagnosis="RAM Failure" , recommendation="Reseat or replace RAM."))

    @Rule(Fact(action="diagnose"),
          Fact(symptom="clicking_noise_from_hard_drive"),
          OR (Fact(symptom="slow_performance"), Fact(symptom="frequent_freezing")))
    def hard_drive_failure(self):
        self.declare(Fact(diagnosis="Hard Drive Failure" , recommendation="Backup data and replace the hard drive."))

    @Rule(Fact(action="diagnose"),
         OR ( Fact(symptom="high_cpu_temperature"),Fact(symptom="sudden_shutdown")))
    def overheating(self):
        self.declare(Fact(diagnosis="Overheating" , recommendation="Clean fans and apply thermal paste."))

    @Rule(Fact(action="diagnose"),
        Fact(symptom="overheating"),  Fact(symptom="computer_does_not_start_after_shutdown"))
    def cpu_failure(self):
        self.declare(Fact(diagnosis="CPU Failure", recommendation="Replace the CPU."))

    @Rule(Fact(action="diagnose"),
          OR(Fact(symptom="no_display"),
          Fact(symptom="artifacts_on_screen")))
    def gpu_failure(self):
        self.declare(Fact(diagnosis="GPU Failure" , recommendation="Reseat or replace the GPU."))

    @Rule(Fact(action="diagnose"),
          Fact(symptom="no_post"),
          NOT(Fact(symptom="power_supply_failure")))
    def motherboard_issue(self):
        self.declare(Fact(diagnosis="Motherboard Issue", recommendation="Check motherboard connections or replace it."))

    @Rule(Fact(action="diagnose"),
     OR  (   Fact(symptom="frequent_application_crashes"),  Fact(symptom="os_boot_loop")))
    def software_corruption(self):
        self.declare(Fact(diagnosis="Software Corruption" , recommendation="Reinstall software or operating system."))

    @Rule(Fact(action="diagnose"),
          OR(Fact(symptom="keyboard_mouse_not_detected"),
          Fact(symptom="usb_devices_not_recognized")))
    def faulty_peripherals(self):
        self.declare(Fact(diagnosis="Faulty Peripherals" , recommendation="Check or replace peripherals."))
    @Rule(Fact(action="diagnose"),
          Fact(symptom="overheating"),
          Fact(symptom="fans_not_spinning"))
    def cooling_system_failure(self):
        self.declare(Fact(diagnosis="Cooling System Failure" , recommendation="Replace or repair the cooling system."))

    @Rule(Fact(action="diagnose"),
          Fact(diagnosis="Power_Supply_Failure"),
          Fact(symptom="random_component_malfunctions"))
    def power_surge_damage(self):
        self.declare(Fact(diagnosis="Power Surge Damage" , recommendation="Check and replace affected components."))

    @Rule(Fact(action="diagnose"),
          Fact(symptom="no_internet_access"),
          OR(Fact(symptom="network_adapter_not_detected"), Fact(symptom="intermittent_connectivity")))
    def faulty_network_adapter(self):
        self.declare(Fact(diagnosis="Faulty Network Adapter" , recommendation="Reinstall drivers or replace the network adapter."))

    @Rule(Fact(action="diagnose"),
          OR(Fact(symptom="bios_settings_reset"), Fact(symptom="incorrect_system_clock")))
    def cmos_battery_failure(self):
        self.declare(Fact(diagnosis="CMOS Battery Failure" , recommendation="Replace the CMOS battery."))

    @Rule(Fact(action="diagnose"),
         OR( Fact(symptom="hard_drive_failure"),
          Fact(symptom="other_drives_not_detected")))
    def faulty_storage_controller(self):
        self.declare(Fact(diagnosis="Faulty Storage Controller" , recommendation="Replace the storage controller."))

    @Rule(Fact(action="diagnose"),
         OR( Fact(symptom="new_hardware_installed"),
          Fact(symptom="os_crashes")))
    def driver_conflict(self):
        self.declare(Fact(diagnosis="Driver Conflict" , recommendation="Update or reinstall drivers."))

    @Rule(Fact(action="diagnose"),
         OR( Fact(symptom="multiple_components_connected"),
          Fact(symptom="random_shutdowns")))
    def insufficient_power_supply(self):
        self.declare(Fact(diagnosis="Insufficient Power Supply Capacity" , recommendation="Upgrade the power supply."))

    @Rule(Fact(action="diagnose"),
          Fact(symptom="overheating"),
          OR(Fact(symptom="high_fan_noise"), Fact(symptom="reduced_cooling_performance")))
    def excessive_dust(self):
        self.declare(Fact(diagnosis="Excessive Dust Build-Up" , recommendation="Clean internal components thoroughly."))



# Main application with an inspiring design
class ExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💻 Computer Fault Diagnosis System")
        self.root.geometry("1200x800")  # Adjusted for larger screens
        self.root.configure(bg="#f4f8f9")  # Light grayish-blue background

        # Fonts and Colors
        self.title_font = ("Helvetica", 28, "bold")
        self.subtitle_font = ("Helvetica", 16, "bold")
        self.button_font = ("Helvetica", 14, "bold")
        self.primary_color = "#2f4f6f"  # Deep teal blue
        self.secondary_color = "#ffffff"  # White
        self.accent_color = "#3db4b4"  # Vibrant teal

        # Initialize Main Menu
        self.create_main_menu()

    def create_main_menu(self):
        """Create the main menu interface"""
        self.clear_frame()

        # Header with gradient
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=100)
        header_frame.pack(fill="x")
        title = tk.Label(
            header_frame,
            text="💻 Computer Fault Diagnosis System",
            font=self.title_font,
            bg=self.primary_color,
            fg=self.secondary_color,
        )
        title.place(relx=0.5, rely=0.5, anchor="center")

        # Content frame with white background and some padding
        content_frame = tk.Frame(self.root, bg=self.secondary_color, width=1000, height=500, padx=40, pady=40)
        content_frame.pack(pady=50)
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Select symptoms subtitle
        subtitle = tk.Label(
            content_frame,
            text="Select your diagnostic method 🔧",
            font=self.subtitle_font,
            bg=self.secondary_color,
            fg=self.primary_color,
        )
        subtitle.pack(pady=20)

        # Forward Chaining Button
        forward_button = tk.Button(
            content_frame,
            text="🚀 Forward Chaining",
            font=self.button_font,
            bg=self.accent_color,
            fg="white",
            relief="flat",
            command=self.forward_chaining_interface,
            width=20,
            height=2,
            bd=0,
            activebackground=self.accent_color,
        )
        forward_button.pack(pady=20)

        # Backward Chaining Button
        backward_button = tk.Button(
            content_frame,
            text="🔄 Backward Chaining",
            font=self.button_font,
            bg=self.accent_color,
            fg="white",
            relief="flat",
            command=self.backward_chaining_interface,
            width=20,
            height=2,
            bd=0,
            activebackground=self.accent_color,
        )
        backward_button.pack(pady=20)

    def forward_chaining_interface(self):
        """Create forward chaining interface"""
        self.clear_frame()
        self.add_header("🚀 Forward Chaining - Select Symptoms")

        # Main body
        body_frame = tk.Frame(self.root, bg="#ffffff", padx=40, pady=20)
        body_frame.pack(expand=True, fill="both" ,  padx=20, pady=20)
        # Create a canvas widget
        canvas = tk.Canvas(body_frame, bg="#ffffff", width=900, height=500)
        canvas.pack(side="left", fill="both", expand=True)

        # Create a scrollbar linked to the canvas
        scrollbar = tk.Scrollbar(body_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold all symptoms inside the canvas
        symptom_frame = tk.Frame(canvas, bg="#ffffff")
        canvas.create_window((0, 0), window=symptom_frame, anchor="nw")

        # Symptoms Selection
        tk.Label(symptom_frame, text="📋 Choose symptoms:", font=self.subtitle_font, bg=body_frame["bg"]).pack(pady=20)
        self.symptom1 = tk.BooleanVar()
        self.symptom2 = tk.BooleanVar()
        tk.Checkbutton(
            symptom_frame, text="💻 Computer doesn't start", variable=self.symptom1, bg=body_frame["bg"], font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        tk.Checkbutton(
            symptom_frame,
            text="🔇 No fan noise ",
            variable=self.symptom2,
            bg=body_frame["bg"],
            font=self.subtitle_font,
        ).pack(anchor="w", padx=20)

        self.symptom3 = tk.BooleanVar()
        tk.Checkbutton(
            symptom_frame,
            text="NO LED indicators",
            variable=self.symptom3,
            bg=body_frame["bg"],
            font=self.subtitle_font,
        ).pack(anchor="w", padx=20)


        # Additional symptoms for other conditions
        self.symptom33 = tk.BooleanVar()
        tk.Checkbutton(
            symptom_frame,
            text="🛑 Random crashes",
            variable=self.symptom33,
            bg=body_frame["bg"],
            font=self.subtitle_font,
        ).pack(anchor="w", padx=20)

        # Symptom 4: Blue screen 
        self.symptom4 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
         text="❌ Blue screen ",
         variable=self.symptom4,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

         # Symptom :  system beeps during startup
        self.symptom44 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
         text="❌ system beeps during startup",
         variable=self.symptom44,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 5: High CPU temperature 
        self.symptom5 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="🌡️High CPU temperature ",
         variable=self.symptom5,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom :  sudden shutdown
        self.symptom55 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="sudden shutdown",
         variable=self.symptom55,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 6: Slow performance 
        self.symptom6 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="💾 Slow performance ",
         variable=self.symptom6,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)


         # Symptom : frequent freezing hhhhhhhhhhhhhhhhhhhhhhnaaaaaaaaaaaa0
        self.symptom66 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="frequent freezing",
         variable=self.symptom66,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)


        #symthon : no display 
        self.symptom00 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="No display",
         variable=self.symptom00,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)


        # artificats onn the screen
        self.symptom022 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="artificats on the screen",
         variable=self.symptom022,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
   
        # Symptom 7: Clicking noise from the hard drive
        self.symptom7 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
         text="🔊 Clicking noise from the hard drive",
         variable=self.symptom7,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 8: Overheating 
        self.symptom8 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
         text="🔥 Overheating ",
         variable=self.symptom8,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # Symptom : fans not spinning
        self.symptom88 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
         text=" fans not spinning",
         variable=self.symptom88,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom : computer doesnt start after shutdown
        self.symptom999 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
         text="computer doesnt start after shutdown",
         variable=self.symptom999,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        #no post
        self.symptom999 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="no post",
         variable=self.symptom999,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # Symptom 9: Power supply failure 
        self.symptom9 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
         text="⚡ Power supply failure ",
         variable=self.symptom9,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # Symptom 9: random component malfunctions
        self.symptom99 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
         text="⚡  random component malfunctions",
         variable=self.symptom99,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 10: network adapter not detected 
        self.symptom100 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="🌐 network adapter issues",
         variable=self.symptom100,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # Symptom 10: No internet access 
        self.symptom10 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="🌐 No internet access ",
         variable=self.symptom10,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # Symptom  :intermittent connectivity
        self.symptom110 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="intermittent connectivity",
         variable=self.symptom110,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)



        # Symptom 11: BIOS settings reset after shutdown 
        self.symptom11 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="🔋 BIOS settings reset after shutdown ",
         variable=self.symptom11,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 11:  incorrect system clock
        self.symptom111 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="incorrect system clock",
         variable=self.symptom111,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 12: Hard drive failure 
        self.symptom12 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
          text="💔 Hard drive failure ",
         variable=self.symptom12,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # Symptom 12: other drives not detected
        self.symptom122 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
          text="other drives not detected",
         variable=self.symptom122,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 13: New hardware installed 
        self.symptom13 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
          text="🆕 New hardware installed ",
          variable=self.symptom13,
          bg=body_frame["bg"],
          font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # Symptom : operating system crashes
        self.symptom133 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
          text="🆕 OS crashes",
          variable=self.symptom133,
          bg=body_frame["bg"],
          font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # frequent app crashes 
        self.symptom69 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
          text="frequent application crashes",
          variable=self.symptom69,
          bg=body_frame["bg"],
          font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # operating system boot loop
        self.symptom70 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
          text="operating system boot loop",
          variable=self.symptom70,
          bg=body_frame["bg"],
          font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 14: Multiple components connected 
        self.symptom14 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="🔌 Multiple components connected",
         variable=self.symptom14,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # Symptom random shutdowns
        self.symptom144 = tk.BooleanVar()
        tk.Checkbutton(
         symptom_frame,
         text="random shutdowns",
         variable=self.symptom144,
         bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        # Symptom 15: High fan noise 
        self.symptom15 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
          text="🌀 High fan noise ",
          variable=self.symptom15,
          bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
         # Symptom 15:  reduced cooling performance due to dust
        self.symptom155 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
          text="reduced cooling performance due to dust",
          variable=self.symptom155,
          bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)

        #key... /mouse not detected
        self.symptom89 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
          text="keyboard /mouse not detected ",
          variable=self.symptom89,
          bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)
        # usb devices not recongnized
        self.symptom90 = tk.BooleanVar()
        tk.Checkbutton(
          symptom_frame,
          text="USB devices not recognized",
          variable=self.symptom90,
          bg=body_frame["bg"],
         font=self.subtitle_font
        ).pack(anchor="w", padx=20)






        # Update scroll region for the canvas
        symptom_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Diagnose Button
        tk.Button(
            body_frame,
            text="🔍 Diagnose",
            font=self.button_font,
            bg=self.primary_color,
            fg="white",
            command=self.forward_diagnose,
            width=15,
            height=2,
        ).pack(pady=20)

        # Back Button
        self.add_back_button(body_frame, self.create_main_menu)

    def forward_diagnose(self):
        """Perform forward chaining diagnosis"""
        engine = ComputerDiagnosis()
        engine.reset()

        # Add symptoms based on user selection
        if self.symptom1.get():
            engine.declare(Fact(symptom="computer_does_not_start"))
        if self.symptom2.get():
            engine.declare(Fact(symptom="no_fan"))
        if self.symptom3.get():
            engine.declare(Fact(symptom="no_led"))
        if self.symptom33.get():
            engine.declare(Fact(symptom="random_crashes"))
        if self.symptom4.get():
            engine.declare(Fact(symptom="blue_screen"))
        if self.symptom44.get():
            engine.declare(Fact(symptom="beeps"))

        if self.symptom6.get():
            engine.declare(Fact(symptom="slow_performance"))
        if self.symptom66.get():
            engine.declare(Fact(symptom="frequent_freezing"))
        if self.symptom7.get():
            engine.declare(Fact(symptom="clicking_noise_from_hard_drive"))

        if self.symptom5.get():
            engine.declare(Fact(symptom="high_cpu_temperature"))
        if self.symptom55.get():
            engine.declare(Fact(symptom="sudden_shutdown"))
            #updateeeeeeeeeeeeeee
        if self.symptom8.get():
            engine.declare(Fact(symptom="overheating"))
        if self.symptom999.get():
            engine.declare(Fact(symptom="computer_does_not_start_after_shutdown"))
        if self.symptom88.get():
            engine.declare(Fact(symptom="fans_not_spinning"))
            

        if self.symptom00.get():
            engine.declare(Fact(symptom="no_display"))
        if self.symptom022.get():
            engine.declare(Fact(symptom="artifacts_on_screen"))

        if self.symptom999.get():
            engine.declare(Fact(symptom="no_post"))
        if self.symptom9.get():
            engine.declare(Fact(symptom="Power_Supply_Failure"))
        if self.symptom99.get():
            engine.declare(Fact(symptom="random_component_malfunctions"))
            
        if self.symptom100.get():
            engine.declare(Fact(symptom="network_adapter_not_detected"))
        if self.symptom10.get():
            engine.declare(Fact(symptom="no_internet_access"))
        if self.symptom110.get():
            engine.declare(Fact(symptom="intermittent_connectivity"))
            

        if self.symptom69.get():
            engine.declare(Fact(symptom="frequent_application_crashes"))
        if self.symptom70.get():
            engine.declare(Fact(symptom="os_boot_loop"))


        if self.symptom89.get():
            engine.declare(Fact(symptom="keyboard_mouse_not_detected"))
        if self.symptom90.get():
            engine.declare(Fact(symptom="usb_devices_not_recognized"))

        if self.symptom11.get():
            engine.declare(Fact(symptom="bios_settings_reset"))
        if self.symptom111.get():
            engine.declare(Fact(symptom="incorrect_system_clock"))

        if self.symptom12.get():
            engine.declare(Fact(symptom="hard_drive_failure"))
        if self.symptom122.get():
            engine.declare(Fact(symptom="other_drives_not_detected"))

        if self.symptom13.get():
            engine.declare(Fact(symptom="new_hardware_installed"))
        if self.symptom133.get():
            engine.declare(Fact(symptom="os_crashes"))

        if self.symptom14.get():
            engine.declare(Fact(symptom="multiple_components_connected"))
        if self.symptom144.get():
            engine.declare(Fact(symptom="random_shutdowns"))

        if self.symptom15.get():
            engine.declare(Fact(symptom="high_fan_noise"))
        if self.symptom155.get():
            engine.declare(Fact(symptom="reduced_cooling_performance"))





        engine.run()

        # Retrieve results
        diagnosis = None
        recommendation = None
        for fact in engine.facts.values():
            if fact.get("diagnosis"):
                diagnosis = fact["diagnosis"]
            if fact.get("recommendation"):
                recommendation = fact["recommendation"]

        # Display results
        if diagnosis:
            messagebox.showinfo("Diagnosis ✅", f"Diagnosis: {diagnosis}\nRecommendation: {recommendation}")
        else:
            messagebox.showinfo("Diagnosis ❌", "Unable to diagnose based on the selected symptoms.")

    def backward_chaining_interface(self):
     """Create backward chaining interface"""
     self.clear_frame()
     self.add_header("🔄 Backward Chaining - Select Symptoms")

    # Main body
     body_frame = tk.Frame(self.root, bg="#ffffff", padx=40, pady=20)
     body_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Create a canvas widget for scrolling
     canvas = tk.Canvas(body_frame, bg="#ffffff", width=900, height=500)
     canvas.pack(side="left", fill="both", expand=True)

    # Create a scrollbar linked to the canvas
     scrollbar = tk.Scrollbar(body_frame, orient="vertical", command=canvas.yview)
     scrollbar.pack(side="right", fill="y")

     canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold all symptoms inside the canvas
     symptom_frame = tk.Frame(canvas, bg="#ffffff")
     canvas.create_window((0, 0), window=symptom_frame, anchor="nw")

    # Symptoms selection variables
     symptoms_vars = {
    "computer_does_not_start": tk.BooleanVar(),
    "no_fan": tk.BooleanVar(),
    "no_led": tk.BooleanVar(),
    "random_crashes": tk.BooleanVar(),
    "blue_screen": tk.BooleanVar(),
    "beeps": tk.BooleanVar(),
    "clicking_noise_from_hard_drive": tk.BooleanVar(),
    "slow_performance": tk.BooleanVar(),
    "frequent_freezing": tk.BooleanVar(),
    "high_cpu_temperature": tk.BooleanVar(),
    "sudden_shutdown": tk.BooleanVar(),
    "overheating": tk.BooleanVar(),
    "computer_does_not_start_after_shutdown": tk.BooleanVar(),
    "no_display": tk.BooleanVar(),
    "artifacts_on_screen": tk.BooleanVar(),
    "no_post": tk.BooleanVar(),
    "frequent_application_crashes": tk.BooleanVar(),
    "os_boot_loop": tk.BooleanVar(),
    "keyboard_mouse_not_detected": tk.BooleanVar(),
    "usb_devices_not_recognized": tk.BooleanVar(),
    "fans_not_spinning": tk.BooleanVar(),
    "random_component_malfunctions": tk.BooleanVar(),
    "no_internet_access": tk.BooleanVar(),
    "network_adapter_not_detected": tk.BooleanVar(),
    "intermittent_connectivity": tk.BooleanVar(),
    "bios_settings_reset": tk.BooleanVar(),
    "incorrect_system_clock": tk.BooleanVar(),
    "hard_drive_failure": tk.BooleanVar(),
    "other_drives_not_detected": tk.BooleanVar(),
    "new_hardware_installed": tk.BooleanVar(),
    "os_crashes": tk.BooleanVar(),
    "multiple_components_connected": tk.BooleanVar(),
    "random_shutdowns": tk.BooleanVar(),
    "high_fan_noise": tk.BooleanVar(),
    "reduced_cooling_performance": tk.BooleanVar(),
     }

    # Symptoms list with labels
     symptoms_list = [
    ("💻 Computer does not start", "computer_does_not_start"),
    ("🔇 No fan", "no_fan"),
    ("❌ No LED", "no_led"),
    ("🛑 Random crashes", "random_crashes"),
    ("❌ Blue screen", "blue_screen"),
    ("🔊 Beeps", "beeps"),
    ("🔊 Clicking noise from hard drive", "clicking_noise_from_hard_drive"),
    ("💾 Slow performance", "slow_performance"),
    ("🔄 Frequent freezing", "frequent_freezing"),
    ("🌡️ High CPU temperature", "high_cpu_temperature"),
    ("⚡ Sudden shutdown", "sudden_shutdown"),
    ("🔥 Overheating", "overheating"),
    ("💻 Computer does not start after shutdown", "computer_does_not_start_after_shutdown"),
    ("🖥️ No display", "no_display"),
    ("🖼️ Artifacts on screen", "artifacts_on_screen"),
    ("❌ No POST", "no_post"),
    ("🛑 Frequent application crashes", "frequent_application_crashes"),
    ("🔄 OS boot loop", "os_boot_loop"),
    ("⌨️ Keyboard/mouse not detected", "keyboard_mouse_not_detected"),
    ("📡 USB devices not recognized", "usb_devices_not_recognized"),
    ("🌪️ Fans not spinning", "fans_not_spinning"),
    ("🔄 Random component malfunctions", "random_component_malfunctions"),
    ("🌐 No internet access", "no_internet_access"),
    ("📶 Network adapter not detected", "network_adapter_not_detected"),
    ("🔌 Intermittent connectivity", "intermittent_connectivity"),
    ("⚙️ BIOS settings reset", "bios_settings_reset"),
    ("⏰ Incorrect system clock", "incorrect_system_clock"),
    ("💿 Hard drive failure", "hard_drive_failure"),
    ("📁 Other drives not detected", "other_drives_not_detected"),
    ("🆕 New hardware installed", "new_hardware_installed"),
    ("💥 OS crashes", "os_crashes"),
    ("🔌 Multiple components connected", "multiple_components_connected"),
    ("🔄 Random shutdowns", "random_shutdowns"),
    ("🌬️ High fan noise", "high_fan_noise"),
    ("❄️ Reduced cooling performance", "reduced_cooling_performance"),

        ]

    # Create checkbuttons for symptoms
     tk.Label(symptom_frame, text="📋 Choose symptoms:", 
             font=self.subtitle_font, bg=body_frame["bg"]).pack(pady=20)

     for label, var_name in symptoms_list:
        tk.Checkbutton(
            symptom_frame, 
            text=label, 
            variable=symptoms_vars[var_name], 
            bg=body_frame["bg"], 
            font=self.subtitle_font
        ).pack(anchor="w", padx=20)

    # Update scroll region for the canvas
     symptom_frame.update_idletasks()
     canvas.config(scrollregion=canvas.bbox("all"))

    # Diagnose Button
     tk.Button(
        body_frame,
        text="🔍 Diagnose",
        font=self.button_font,
        bg=self.primary_color,
        fg="white",
        command=lambda: self.backward_diagnose(symptoms_vars),
        width=15,
        height=2,
    ).pack(pady=20)

    # Back Button
     self.add_back_button(body_frame, self.create_main_menu)

    def backward_diagnose(self, symptoms_vars):
     """Perform backward chaining diagnosis based on selected symptoms."""
    
    # Initialize the expert system engine
     engine = ComputerDiagnosis()
     engine.reset()

    # Declare initial action
     engine.declare(Fact(action="diagnose"))

    # Declare user-selected symptoms as facts
     for symptom, var in symptoms_vars.items():
         if var.get():
             engine.declare(Fact(symptom=symptom))

    # Run the engine to process the facts and rules
     engine.run()

    # Retrieve the diagnosis and recommendation
     diagnosis = None
     recommendation = None
     for fact in engine.facts.values():
        # Retrieve diagnosis and recommendation from the declared facts
         if "diagnosis" in fact:
             diagnosis = fact["diagnosis"]
         if "recommendation" in fact:
             recommendation = fact["recommendation"]

    # Display the diagnosis and recommendation, or inform the user if none found
     if diagnosis and recommendation:
         messagebox.showinfo(
            "Diagnosis ✅", 
            f"Diagnosis: {diagnosis}\nRecommendation: {recommendation}"
        )
     else:
        messagebox.showinfo(
            "Diagnosis ❌", 
            "Unable to diagnose based on the selected symptoms."
        )

         

    def clear_frame(self):
        """Clear current frame content"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_header(self, text):
        """Add header to a new page"""
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=100)
        header_frame.pack(fill="x")
        title = tk.Label(
            header_frame,
            text=text,
            font=self.title_font,
            bg=self.primary_color,
            fg=self.secondary_color,
        )
        title.place(relx=0.5, rely=0.5, anchor="center")

    def add_back_button(self, frame, back_function):
        """Add back button to a frame"""
        back_button = tk.Button(
            frame,
            text="◀️ Back",
            font=self.button_font,
            bg=self.accent_color,
            fg="white",
            relief="flat",
            command=back_function,
            width=10,
            height=2,
            bd=0,
            activebackground=self.accent_color,
        )
        back_button.pack(pady=20)

# Create and run the app
root = tk.Tk()
app = ExpertSystemApp(root)
root.mainloop()