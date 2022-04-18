import reapy
from reapy import reascript_api as RPR

import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t1', dest='timestamp_start', required=True, help='start position.')
    parser.add_argument('-t2', dest='timestamp_stop', required=True, help='stop position.')
    parser.add_argument('-elev', dest='elevation_values', required=True,
                        help='elevation values for Panorama parameter.')
    parser.add_argument('-azim', dest='azimuth_values', required=True, help='azimuth values for Panorama parameter.')
    args = parser.parse_args()

    return args


def reaper_connector(t1, t2, elev_list, az_list):
    """
    Parse argument for Reaper command line. Print performed action name.
    """
    print(sys.path)
    project = reapy.Project()
    sample_track = project.tracks[0]

    # if opt in ("-p", "--play"):
    #     project.play()
    #     reapy.print("Play")
    #
    # elif opt in ("-s", "--stop"):
    #     project.stop()
    #     reapy.print("Stop")
    #
    # elif opt in ("-R", "--referenceOn"):
    #     sample_track.unmute()
    #     reapy.print("2nd track unmuted")
    #
    # elif opt in ("-r", "--referenceMute"):
    #     sample_track.mute()
    #     reapy.print("2nd track muted")
    #
    # elif opt in ("-n", "--n1toff"):
    #     reference_track.fxs[0].disable()
    #     reapy.print("Noise disabled on first track")
    #
    # elif opt in ("-N", "--n1ton"):
    #     reference_track.fxs[0].enable()
    #     reapy.print("Noise enabled on first track")
    #
    # elif opt in ("-b", "--n2toff"):
    #     sample_track.fxs[0].disable()
    #     reapy.print("Noise disabled on second track")
    #
    # elif opt in ("-B", "--n2ton"):
    #     sample_track.fxs[0].enable()
    #     reapy.print("Noise enabled on second track")

    # elif opt in ("-m", "--marker"):
    #     marker_idx = int(arg) - 1
    #     marker = project.markers[marker_idx]
    #     project.cursor_position = marker.position
    #     reapy.print("Move to marker " + arg)
    #
    # elif opt in ("-f", "--findParams"):
    #     params = sample_track.fxs[1].params
    #     for param in params:
    #         reapy.print(param.name)
    #         reapy.print(param)

    if elev_list and az_list:
        pos = 1
        const = 0.1
        for el, az in zip(elev_list, az_list):
            angle_az = (float(az) + 180) / 360
            angle_el = (float(el) + 180) / 360

            change_param('Azimuth Angle / StereoEncoder', angle_az, sample_track, pos, const)
            change_param('Elevation Angle / StereoEncoder', angle_el, sample_track, pos, const)
            pos += const


def change_param(param, angle, track, time, const):
    """
    :param: azimuth/elevation
    :arg: angle value given by user

    Range of azimuth/elevation angle is (0 360) degrees.
    Reduce argument value by 180 degrees to adjust for Reaper plugin scope.
    Plugin accepts argument value in range (0 1) which correspond to (-180, 180) angle degrees.
    """
    try:
        envelopes = track.envelopes
        for env in envelopes:
            if env.name == param:
                automation_item = env.add_item(position=time, length=const, pool=-2)
                automation_item.set_value(time, angle)
                reapy.print('=======================')
                reapy.print('=======================')

    except Exception as exc:
        reapy.print(exc)


def main():
    args = parse_args()

    try:
        reaper_connector(args.timestamp_start, args.timestamp_stop, args.elevation_values, args.azimuth_values)
    except Exception:
        print("exception")
