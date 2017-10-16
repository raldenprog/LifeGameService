import React from 'react'
import FolderIcon from 'react-icons/lib/md/folder'
import FileIcon from 'react-icons/lib/md/description'


const normalizeSize = (size) =>
  size/1024 > 999
  ? `${Math.round(size/1024/1024)} MB`
  : `${Math.round(size/1024)} KB`


export const FileCard = ({params: params}) => (
    <div
      className='list-group-item'
      data-toggle='tooltip'
      title={`Size:${normalizeSize(params.size)}`}>
        <FileIcon size={30} color='gray'/>
        {params.name}
      <div className='tooltip top' role='tooltip'>
        <div className='tooltip-arrow'></div>
        <div className='tooltip-inner'>
          Size
        </div>
      </div>
    </div>
  )


export const FolderCard = ({
    params: params,
    history: history}) =>
    (
      <div
        className='list-group-item'
        onClick={ () =>
        history.push(`${params.path.slice(6)}`)}>
        <FolderIcon size={30} color='gray'/>
        {params.name}
    </div>
  )
