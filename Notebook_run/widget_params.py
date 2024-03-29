from IPython.display import display
import ipywidgets as widgets
from ipywidgets import FloatSlider, Dropdown, Layout, HBox, RadioButtons

def widget_interact_manual_current(mode):
    if mode == 'pulse':
        style = {'description_width': 'initial'}
        gks= widgets.FloatSlider(value = 13.40, min = 12, max = 30,
                        description='Slow potassium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '400px'), style = style)

        gcal= widgets.FloatSlider(value = 0.0172, min = 0.0001, max = 0.062,
                        description='L-type calcium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '400px'), style = style, readout_format='.4f')

        gnap= widgets.FloatSlider(value = 1.91, min = 0.1, max = 3,
                        description='Persistent sodium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '400px'), style = style)

        mutype = widgets.Dropdown(options = ['S', 'FR', 'FF'], value = 'FF',
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Motor neuron type:', style = style)

        gama = widgets.Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Monoaminergic drive:', style = style)

        delay = widgets.Dropdown(options = range(0,300,10), value = 290,
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Injected current delay [$ms$]:', style = style)

        predur= widgets.FloatSlider(value = 1500, min = 0, max = 5000,
                        description='Depolarizing current pulse duration [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        meddur= widgets.FloatSlider(value = 3000, min = 0, max = 5000,
                        description='Time between current pulses [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        posdur= widgets.FloatSlider(value = 1000, min = 0, max = 5000,
                        description='Hyperpolarizing current pulse duration [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        preamp= widgets.FloatSlider(value = 20, min = -30, max = 50,
                        description='Depolarizing current pulse amplitude [$nA$]:', 
                        layout = Layout(width= '400px'), style = style)

        posamp= widgets.FloatSlider(value = -50, min = -50, max = 50,
                        description='Hyperpolarizing current pulse amplitude [$nA$]:', 
                        layout = Layout(width= '400px'), style = style)

        ld= widgets.FloatSlider(value = 12049, min = 1000, max = 25000,
                        description='Dendrite length [$\mu m$]:', 
                        layout = Layout(width= '400px'), style = style)

        diam = widgets.FloatSlider(value = 93, min = 10, max = 300,
                        description='Dendrite diameter [$\mu m$]:', 
                        layout = Layout(width= '400px'), style = style)
        return [mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks]
    
    elif mode == 'triangular':
        style = {'description_width': 'initial'}
        gks= FloatSlider(value = 13.40, min = 12, max = 30,
                        description='Slow potassium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '400px'), style = style)

        gcal= FloatSlider(value = 0.0172, min = 0.0001, max = 0.062,
                        description='L-type calcium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '400px'), style = style, readout_format='.4f')

        gnap= FloatSlider(value = 1.91, min = 0.1, max = 3,
                        description='Persistent sodium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '400px'), style = style)

        mutype = Dropdown(options = ['S', 'FR', 'FF'], value = 'FF',
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Motor neuron type:', style = style)

        gama = Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Monoaminergic drive:', style = style)

        delay = Dropdown(options = range(0,300,10), value = 20,
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Injected current delay [$ms$]:', style = style)

        predur= FloatSlider(value = 3000, min = 0, max = 3000,
                        description='Ascending phase duration [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        posdur= FloatSlider(value = 5000, min = 0, max = 6000,
                        description='Descending phase duration [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        posamp= FloatSlider(value = 20, min = -100, max = 50,
                        description='Peak amplitude [$nA$]:', 
                        layout = Layout(width= '400px'), style = style)
        possamp= FloatSlider(value = -10, min = -100, max = 50,
                        description='Final amplitude [$nA$]:', 
                        layout = Layout(width= '400px'), style = style)

        ld= FloatSlider(value = 12049, min = 1000, max = 25000,
                        description='Dendrite length [$\mu m$]:', 
                        layout = Layout(width= '400px'), style = style)

        diam= FloatSlider(value = 93, min = 10, max = 300,
                        description='Dendrite diameter [$\mu m$]:', 
                        layout = Layout(width= '400px'), style = style)
        return [mutype,gama,delay,predur,posdur,posamp, possamp,ld,diam,gnap,gcal,gks]
    else:
        print("mode not found")

        

def widget_params_pulse():

    style = {'description_width': 'initial'}
    gks= widgets.FloatSlider(value = 13.40, min = 12, max = 30,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    gcal= widgets.FloatSlider(value = 0.0172, min = 0.0001, max = 0.062,
                    description='L-type calcium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style, readout_format='.4f')

    gnap= widgets.FloatSlider(value = 1.91, min = 0.0001, max = 3,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    mutype = widgets.Dropdown(options = ['S', 'FR', 'FF'], value = 'FF',
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Motor neuron type:', style = style)

    gama = widgets.Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Monoaminergic drive:', style = style)

    delay = widgets.Dropdown(options = range(0,300,10), value = 290,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    predur= widgets.FloatSlider(value = 1500, min = 0, max = 5000,
                    description='Depolarizing current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    meddur= widgets.FloatSlider(value = 3000, min = 0, max = 5000,
                    description='Time between current pulses [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posdur= widgets.FloatSlider(value = 1000, min = 0, max = 5000,
                    description='Hyperpolarizing current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    preamp= widgets.FloatSlider(value = 20, min = -30, max = 50,
                    description='Depolarizing current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    posamp= widgets.FloatSlider(value = -50, min = -50, max = 50,
                    description='Hyperpolarizing current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    ld= widgets.FloatSlider(value = 12049, min = 1000, max = 25000,
                    description='Dendrite length [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam = widgets.FloatSlider(value = 93, min = 10, max = 300,
                    description='Dendrite diameter [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)
   
    parameters = widgets.VBox([mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks])
    wp = {'mutype':mutype,'gama': gama, 'delay':delay,'predur': predur,'meddur': meddur,'posdur': posdur,'preamp': preamp,'posamp':posamp,'ld':ld,'diam':diam, 'gnap':gnap, 'gcal':gcal, 'gks':gks}

    for i in parameters.children:
        i.layout = widgets.Layout(width= '400px')
        i.style = style
        i.continuous_update = False
    return parameters,wp
 
    
def widget_params_interact_manual_pulse():

    style = {'description_width': 'initial'}
    gks= widgets.FloatSlider(value = 13.40, min = 12, max = 30,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    gcal= widgets.FloatSlider(value = 0.0172, min = 0.0001, max = 1.0000,
                    description='L-type calcium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style, readout_format='.4f')

    gnap= widgets.FloatSlider(value = 1.91, min = 0.1, max = 3,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    mutype = widgets.Dropdown(options = ['S', 'FR', 'FF'], value = 'FF',
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Motor neuron type:', style = style)

    gama = widgets.Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Monoaminergic drive:', style = style)

    delay = widgets.Dropdown(options = range(0,300,10), value = 290,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    predur= widgets.FloatSlider(value = 1500, min = 0, max = 5000,
                    description='Depolarizing current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    meddur= widgets.FloatSlider(value = 3000, min = 0, max = 5000,
                    description='Time between current pulses [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posdur= widgets.FloatSlider(value = 1000, min = 0, max = 5000,
                    description='Hyperpolarizing current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    preamp= widgets.FloatSlider(value = 20, min = -50, max = 50,
                    description='Depolarizing current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    posamp= widgets.FloatSlider(value = -50, min = -50, max = 50,
                    description='Hyperpolarizing current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    ld= widgets.FloatSlider(value = 12049, min = 1000, max = 25000,
                    description='Dendrite length [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam = widgets.FloatSlider(value = 93, min = 10, max = 300,
                    description='Dendrite diameter [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)
    return [mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks]


def widget_params_triangular():    
    style = {'description_width': 'initial'}
    gks= FloatSlider(value = 13.40, min = 12, max = 30,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    gcal= FloatSlider(value = 0.0172, min = 0.0001, max = 0.062,
                    description='L-type calcium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style, readout_format='.4f')

    gnap= FloatSlider(value = 1.91, min = 0.1, max = 3,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    mutype = Dropdown(options = ['S', 'FR', 'FF'], value = 'FF',
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Motor neuron type:', style = style)

    gama = Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Monoaminergic drive:', style = style)

    delay = Dropdown(options = range(0,300,10), value = 20,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    predur= FloatSlider(value = 3000, min = 0, max = 3000,
                    description='Ascending phase duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posdur= FloatSlider(value = 5000, min = 0, max = 6000,
                    description='Descending phase duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posamp= FloatSlider(value = 20, min = -100, max = 50,
                    description='Peak amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)
    possamp= FloatSlider(value = -10, min = -100, max = 50,
                    description='Final amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    ld= FloatSlider(value = 12049, min = 1000, max = 25000,
                    description='Dendrite length [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam= FloatSlider(value = 93, min = 10, max = 300,
                    description='Dendrite diameter [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)
    
    parameters = widgets.VBox([mutype,gama,delay,predur,posdur,posamp,possamp,ld,diam,gnap,gcal,gks])
    wp = {'mutype':mutype,'gama': gama, 'delay':delay,'posdur': posdur,'predur': predur,'posamp': posamp,'possamp':possamp,'ld':ld,'diam':diam, 'gnap':gnap, 'gcal':gcal, 'gks':gks}

    for i in parameters.children:
        i.layout = widgets.Layout(width= '390px')
        i.style = style
        i.continuous_update = False
    return parameters,wp

def widget_interact_manual_triangular():  
    style = {'description_width': 'initial'}
    gks= FloatSlider(value = 13.40, min = 12, max = 30,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    gcal= FloatSlider(value = 0.0172, min = 0.0001, max = 1.0000,
                    description='L-type calcium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style, readout_format='.4f')

    gnap= FloatSlider(value = 1.91, min = 0.1, max = 3,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    mutype = Dropdown(options = ['S', 'FR', 'FF'], value = 'FF',
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Motor neuron type:', style = style)

    gama = Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Monoaminergic drive:', style = style)

    delay = Dropdown(options = range(0,300,10), value = 20,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    predur= FloatSlider(value = 3000, min = 0, max = 3000,
                    description='Ascending phase duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posdur= FloatSlider(value = 5000, min = 0, max = 6000,
                    description='Descending phase duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posamp= FloatSlider(value = 20, min = -100, max = 50,
                    description='Peak amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)
    possamp= FloatSlider(value = -10, min = -100, max = 50,
                    description='Final amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    ld= FloatSlider(value = 12049, min = 1000, max = 25000,
                    description='Dendrite length [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam= FloatSlider(value = 93, min = 10, max = 300,
                    description='Dendrite diameter [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)
    return [mutype,gama,delay,predur,posdur,posamp,possamp,ld,diam,gnap,gcal,gks]

def widget_action_potential(): 
    style = {'description_width': 'initial'}
    gks= widgets.FloatSlider(value = 16.00, min = 12, max = 30,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    gcal= widgets.FloatSlider(value = 0.0062, min = 0.0001, max = 1.0000,
                    description='L-type calcium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style, readout_format='.4f')

    gnap= widgets.FloatSlider(value = 0.65, min = 0.1, max = 3,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    mutype = widgets.Dropdown(options = ['S', 'FR', 'FF'], value = 'FF',
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Motor neuron type:', style = style)

    gama = widgets.Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 0.2,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Monoaminergic drive:', style = style)

    delay = widgets.Dropdown(options = range(0,300,10), value = 20,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    dur= widgets.FloatSlider(value = 0.5, min = 0, max = 50,
                    description='Injected current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    amp= widgets.FloatSlider(value = 45, min = -50, max = 50,
                    description='Injected current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)
    
    ld= widgets.FloatSlider(value = 9350, min = 1000, max = 25000,
                    description='Dendrite length [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam = widgets.FloatSlider(value = 88, min = 10, max = 300,
                    description='Dendrite diameter [$\mu m$]:', 
                    layout = Layout(width= '400px'), style = style)
    return [mutype,gama,delay,dur,amp,ld,diam,gnap,gcal,gks]
