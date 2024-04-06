import numpy
import matplotlib.pyplot as plt


def amplitude_modulation(sig, t, amp):
    # Define Carrier Signal Characteristics
    carrier_freq = float(input('input frequency of carrier signal: '))
    m = float(input('input modulation index: '))
    carrier_amp = amp / m  # Carrier_amplitude * modulation_index  = Message_signal_amplitude
    carrier_sig = carrier_amp * numpy.cos(numpy.radians(2 * numpy.pi * carrier_freq * t))
    modulated_signal = (1 + m * sig) * carrier_sig
    # Signal Plot
    plt.plot(t, sig)
    # plt.subplot(2, 1, 1)

    # Modulated Signal Plot
    plt.plot(t, modulated_signal)
    # plt.subplot(2, 1, 2)

    plt.xlabel("Time--->")
    plt.ylabel("Signal--->")

    plt.show()


def frequency_modulation(sig, t):
    # Set amplitude of modulated signal and 2 frequencies
    carrier_amp = float(input('input amplitude of modulated signal: '))
    high_freq = float(input('input high frequency of the signal: '))
    low_freq = float(input('input low  frequency of the signal: '))
    high_freq_sig = numpy.array([])
    low_freq_sig = numpy.array([])
    modulated_signal = numpy.array([])
    for i in range(0, len(sig)):
        if sig[i] >= 0:
            high_freq_sig = numpy.append(high_freq_sig, carrier_amp * numpy.cos(numpy.radians(2 * numpy.pi * high_freq * t[i])))
            low_freq_sig = numpy.append(low_freq_sig, 0)
        else:
            low_freq_sig = numpy.append(low_freq_sig, carrier_amp * numpy.cos(numpy.radians(2 * numpy.pi * low_freq * t[i])))
            high_freq_sig = numpy.append(high_freq_sig, 0)
    for i in range(0, len(sig)):
        value = high_freq_sig[i] + low_freq_sig[i]
        modulated_signal = numpy.append(modulated_signal, value)

    # Message Signal
    plt.plot(t, sig)
    # plt.subplot(2, 1, 1)

    # Modulated Signal
    plt.plot(t, modulated_signal)
    # plt.subplot(2, 1, 2)

    plt.xlabel("Time--->")
    plt.ylabel("Signal--->")

    plt.show()


# input message signal characteristics
amp = float(input('input amplitude of the message signal: '))
freq = float(input('input frequency of the message signal: '))
t = numpy.array([x for x in range(0, 1000, 1)]) / 1000
sig = (amp * numpy.cos(numpy.radians(2 * numpy.pi * freq * t)))

# Select Type of Modulation
mod = int(input('Select Modulation: [1. Amplitude Modulation(AM) \n 2. Frequency Modulation(FM) \n:'))
if mod == 1:
    amplitude_modulation(sig, t, amp)
elif mod == 2:
    frequency_modulation(sig, t)
else:
    print('wrong choice')
# print(sig)
# plt.plot(t, sig)
# plt.show()
